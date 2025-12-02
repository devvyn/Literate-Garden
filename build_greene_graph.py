"""Build and analyze an intellectual genealogy graph for Robert Greene.

This script consumes the provided seed JSON, constructs a directed NetworkX graph,
performs influence analyses (shared roots and domain recombination), and exports
a node-link JSON representation.
"""
from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Literal, Optional, Tuple

import networkx as nx
from networkx.readwrite import json_graph

NodeType = Literal["author", "work", "book", "downstream", "collaborator"]
EdgeType = Literal[
    "influenced_by",
    "derives_from",
    "coauthored",
    "apprenticed_under",
    "self_derivative",
    "authored",
]


@dataclass
class Node:
    id: str
    label: str
    type: NodeType
    year: Optional[int] = None
    domain: Optional[str] = None
    role: Optional[str] = None


@dataclass
class Edge:
    src: str
    dst: str
    type: EdgeType
    weight: float = 1.0
    note: Optional[str] = None


def load_seed(seed_path: Path) -> Dict:
    """Load the JSON seed from disk."""
    return json.loads(seed_path.read_text())


def ensure_node(nodes: Dict[str, Node], node: Node) -> None:
    """Add a node if not present, otherwise preserve the existing entry."""
    if node.id not in nodes:
        nodes[node.id] = node


def build_nodes_and_edges(seed: Dict) -> Tuple[List[Node], List[Edge]]:
    """Create the node and edge lists from the seed specification."""
    nodes: Dict[str, Node] = {}
    edges: List[Edge] = []

    # Anchor author node for Greene himself.
    ensure_node(nodes, Node(id="A_ROBERT_GREENE", label="Robert Greene", type="author", role="author"))

    # Greene books
    for book in seed.get("greene_books", []):
        ensure_node(
            nodes,
            Node(
                id=book["id"],
                label=book["title"],
                type="book",
                year=book.get("year"),
                domain="greene_book",
            ),
        )
        edges.append(Edge(src=book["id"], dst="A_ROBERT_GREENE", type="derives_from"))

    # Primary sources and collaborators per book
    for entry in seed.get("seed_sources", []):
        book_id = entry["greene_book_id"]
        for source in entry.get("primary_sources", []):
            source_id = source["id"]
            if source.get("type") == "self_derivative":
                # The Daily Laws draws from earlier Greene works
                ensure_node(nodes, Node(id=source_id, label=source_id, type="book"))
                edges.append(Edge(src=book_id, dst=source_id, type="self_derivative"))
                continue

            ensure_node(
                nodes,
                Node(
                    id=source_id,
                    label=source.get("work", source_id),
                    type="work",
                    domain=source.get("domain"),
                    role="primary_source",
                ),
            )
            note = "reference_only" if source.get("ref_only") else "primary"
            edges.append(Edge(src=book_id, dst=source_id, type="influenced_by", note=note))

        if entry.get("coauthor"):
            coauthor = entry["coauthor"]
            ensure_node(
                nodes,
                Node(id=coauthor["id"], label=coauthor["name"], type="collaborator", role="coauthor"),
            )
            edges.append(Edge(src=entry["greene_book_id"], dst=coauthor["id"], type="coauthored"))

    # Downstream authors and their works
    for downstream in seed.get("downstream_nodes", []):
        ensure_node(
            nodes,
            Node(id=downstream["id"], label=downstream["name"], type="downstream", role=downstream.get("role")),
        )
        for rel in downstream.get("relationship", []):
            edges.append(Edge(src=downstream["id"], dst=rel["to"], type=rel["type"].lower()))
        for work in downstream.get("works", []):
            ensure_node(nodes, Node(id=work["id"], label=work["title"], type="work", domain="downstream"))
            edges.append(Edge(src=work["id"], dst=downstream["id"], type="derives_from"))

    return list(nodes.values()), edges


def build_graph(nodes: Iterable[Node], edges: Iterable[Edge]) -> nx.DiGraph:
    """Instantiate the directed graph."""
    graph = nx.DiGraph()
    for node in nodes:
        graph.add_node(node.id, **asdict(node))
    for edge in edges:
        graph.add_edge(edge.src, edge.dst, **asdict(edge))
    return graph


def shared_root_sources(graph: nx.DiGraph) -> List[Tuple[str, List[str]]]:
    """Sources referenced by more than one Greene book."""
    source_to_books: Dict[str, List[str]] = {}
    for book in [n for n, d in graph.nodes(data=True) if d.get("type") == "book"]:
        for _, target, data in graph.edges(book, data=True):
            if data.get("type") == "influenced_by":
                source_to_books.setdefault(target, []).append(book)

    results: List[Tuple[str, List[str]]] = []
    for source_id, books in sorted(source_to_books.items()):
        unique_books = sorted(set(books))
        if len(unique_books) > 1:
            results.append((source_id, unique_books))
    return results


def cross_domain_recombination(graph: nx.DiGraph) -> Dict[str, Dict]:
    """Domain diversity for each Greene book based on its sources."""
    summary: Dict[str, Dict] = {}
    for book_id, data in graph.nodes(data=True):
        if data.get("type") != "book":
            continue
        domains: List[str] = []
        for _, target, edge_data in graph.edges(book_id, data=True):
            if edge_data.get("type") != "influenced_by":
                continue
            domain = graph.nodes[target].get("domain")
            if domain:
                domains.append(domain)
        unique_domains = sorted(set(domains))
        top_domains = Counter(domains).most_common(3)
        summary[book_id] = {
            "unique_domains": len(unique_domains),
            "top_domains": top_domains,
            "total_sources": len(domains),
        }
    return summary


def describe_graph(graph: nx.DiGraph, shared_roots: List[Tuple[str, List[str]]], domain_mix: Dict[str, Dict]) -> str:
    lines = [
        "Graph Overview",
        f"Nodes: {graph.number_of_nodes()} | Edges: {graph.number_of_edges()}",
        "",
        "Shared Root Sources (influencing multiple books):",
    ]

    if shared_roots:
        for source_id, books in shared_roots:
            label = graph.nodes[source_id].get("label", source_id)
            lines.append(f"- {label}: {', '.join(books)}")
    else:
        lines.append("- None found")

    lines.append("\nCross-domain recombination per book:")
    for book_id, summary in sorted(domain_mix.items(), key=lambda item: graph.nodes[item[0]].get("year", 0)):
        label = graph.nodes[book_id].get("label", book_id)
        top_domains = "; ".join([f"{dom} (x{count})" for dom, count in summary["top_domains"]]) or "n/a"
        lines.append(
            f"- {label}: {summary['unique_domains']} unique domains across {summary['total_sources']} sources | Top: {top_domains}"
        )

    lines.append("\nDownstream influence targets:")
    for node_id, data in graph.nodes(data=True):
        if data.get("type") != "downstream":
            continue
        influenced_by = [dst for _, dst, edata in graph.edges(node_id, data=True) if edata.get("type") in {"influenced_by", "apprenticed_under"}]
        label = data.get("label", node_id)
        lines.append(f"- {label}: influenced by {', '.join(influenced_by) if influenced_by else 'none recorded'}")

    return "\n".join(lines)


def export_graph(graph: nx.DiGraph, output_path: Path) -> None:
    output_path.write_text(json.dumps(json_graph.node_link_data(graph), indent=2))


def main() -> None:
    seed_path = Path(__file__).parent / "greene_graph_seed.json"
    output_path = Path(__file__).parent / "greene_graph_full.json"

    seed = load_seed(seed_path)
    nodes, edges = build_nodes_and_edges(seed)
    graph = build_graph(nodes, edges)

    shared = shared_root_sources(graph)
    domain_mix = cross_domain_recombination(graph)

    export_graph(graph, output_path)
    print(describe_graph(graph, shared, domain_mix))


if __name__ == "__main__":
    main()
