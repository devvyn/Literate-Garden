#!/usr/bin/env python3
"""
Barkour Spec Compliance Auditor

Compares implementation constants against formal specification.
Run from spec/tools/ directory.
"""

import yaml
import json
import re
from pathlib import Path

# Paths relative to this script
SPEC_DIR = Path(__file__).parent.parent
BARKOUR_DIR = SPEC_DIR.parent
PYGAME_DIR = BARKOUR_DIR / "prototypes" / "pygame-movement-01"
SHARED_DIR = BARKOUR_DIR / "shared"


def load_spec():
    """Load MECHANICS.yaml spec values."""
    mechanics_path = SPEC_DIR / "MECHANICS.yaml"
    with open(mechanics_path) as f:
        return yaml.safe_load(f)


def load_shared_config():
    """Load shared/barkour_config.json."""
    config_path = SHARED_DIR / "barkour_config.json"
    with open(config_path) as f:
        return json.load(f)


def extract_pygame_constants(source_path):
    """Extract constant definitions from PyGame main.py."""
    constants = {}
    with open(source_path) as f:
        content = f.read()

    # Match patterns like: CONSTANT_NAME = value
    pattern = r'^([A-Z][A-Z0-9_]+)\s*=\s*(-?[\d.]+)'
    for match in re.finditer(pattern, content, re.MULTILINE):
        name = match.group(1)
        value = float(match.group(2))
        constants[name] = value

    return constants


def audit():
    """Run compliance audit."""
    print("=" * 60)
    print("BARKOUR SPEC COMPLIANCE AUDIT")
    print("=" * 60)
    print()

    # Load sources
    try:
        spec = load_spec()
        print("✓ Loaded MECHANICS.yaml")
    except Exception as e:
        print(f"✗ Failed to load spec: {e}")
        return

    try:
        config = load_shared_config()
        print("✓ Loaded barkour_config.json")
    except Exception as e:
        print(f"✗ Failed to load config: {e}")
        config = None

    try:
        pygame_path = PYGAME_DIR / "main.py"
        pygame_constants = extract_pygame_constants(pygame_path)
        print(f"✓ Extracted {len(pygame_constants)} constants from PyGame")
    except Exception as e:
        print(f"✗ Failed to parse PyGame: {e}")
        pygame_constants = {}

    print()
    print("-" * 60)
    print("PHYSICS CONSTANTS COMPARISON")
    print("-" * 60)
    print()

    # Define mapping: spec path -> (pygame name, config path)
    comparisons = [
        ("physics.gravity.value", "GRAVITY", "physics.gravity"),
        ("physics.terminal_velocity.value", "MAX_FALL_SPEED", "physics.max_fall_speed"),
        ("movement.walk.speed", None, None),  # Spec distinguishes walk/run, impl uses single speed
        ("movement.run.speed", "BASE_MOVEMENT_SPEED", "physics.base_movement_speed"),
        ("jump.force.value", "BASE_JUMP_STRENGTH", "physics.base_jump_strength"),
        ("jump.coyote_time.value", "COYOTE_TIME", "physics.coyote_time_frames"),
        ("jump.jump_buffer.value", "JUMP_BUFFER", "physics.jump_buffer_frames"),
        ("wall.slide.max_fall_speed", "WALL_SLIDE_SPEED", "physics.wall_slide_speed"),
        ("wall.jump.horizontal_force", "WALL_JUMP_PUSH", "physics.wall_jump_push"),
        ("wall.jump.vertical_force", "WALL_JUMP_STRENGTH", "physics.wall_jump_strength"),
        ("bacon.boost.duration.value", "POWERUP_DURATION", "powerup.duration_ms"),
        ("bacon.boost.speed_multiplier.value", "POWERED_SPEED_MULTIPLIER", "powerup.speed_multiplier"),
        ("bacon.boost.jump_multiplier.value", "POWERED_JUMP_MULTIPLIER", "powerup.jump_multiplier"),
    ]

    results = []
    for spec_path, pygame_name, config_path in comparisons:
        # Get spec value
        spec_value = get_nested(spec, spec_path)

        # Get pygame value
        pygame_value = pygame_constants.get(pygame_name) if pygame_name else None

        # Get config value
        config_value = get_nested(config, config_path) if config_path and config else None

        # Convert spec frames to ms for duration comparison
        if "duration" in spec_path and spec_value:
            spec_value_ms = spec_value * (1000 / 60)  # frames to ms at 60fps
            display_spec = f"{spec_value} frames ({spec_value_ms:.0f}ms)"
        else:
            display_spec = spec_value
            spec_value_ms = spec_value

        # Determine match status
        if spec_value is None:
            status = "SPEC_MISSING"
        elif pygame_value is None and pygame_name:
            status = "IMPL_MISSING"
        elif pygame_name is None:
            status = "NEW_IN_SPEC"
        elif "duration" in spec_path:
            # Compare ms values
            if pygame_value and abs(pygame_value - spec_value_ms) < 1:
                status = "MATCH"
            else:
                status = "MISMATCH"
        elif pygame_value is not None and abs(pygame_value - spec_value) < 0.01:
            status = "MATCH"
        else:
            status = "MISMATCH"

        results.append({
            "spec_path": spec_path,
            "spec_value": display_spec,
            "pygame_name": pygame_name,
            "pygame_value": pygame_value,
            "config_value": config_value,
            "status": status,
        })

    # Print results
    for r in results:
        icon = {
            "MATCH": "✓",
            "MISMATCH": "✗",
            "NEW_IN_SPEC": "➕",
            "IMPL_MISSING": "❓",
            "SPEC_MISSING": "⚠",
        }.get(r["status"], "?")

        print(f"{icon} {r['spec_path']}")
        print(f"    Spec:   {r['spec_value']}")
        if r['pygame_name']:
            print(f"    PyGame: {r['pygame_value']} ({r['pygame_name']})")
        if r['config_value'] is not None:
            print(f"    Config: {r['config_value']}")
        if r['status'] not in ("MATCH",):
            print(f"    Status: {r['status']}")
        print()

    # Summary
    print("-" * 60)
    print("SUMMARY")
    print("-" * 60)
    matches = sum(1 for r in results if r["status"] == "MATCH")
    mismatches = sum(1 for r in results if r["status"] == "MISMATCH")
    new_in_spec = sum(1 for r in results if r["status"] == "NEW_IN_SPEC")

    print(f"  Matching:      {matches}")
    print(f"  Mismatches:    {mismatches}")
    print(f"  New in spec:   {new_in_spec}")
    print()

    if mismatches > 0:
        print("ACTION REQUIRED: Reconcile mismatches before certification")
    if new_in_spec > 0:
        print("ACTION REQUIRED: Implement new mechanics or mark optional")


def get_nested(obj, path):
    """Get nested dictionary value by dot path."""
    if obj is None:
        return None
    parts = path.split(".")
    for part in parts:
        if isinstance(obj, dict) and part in obj:
            obj = obj[part]
        else:
            return None
    return obj


if __name__ == "__main__":
    audit()
