"""
Test runner for agent_strata.py - Demonstrates the stacking in action
without requiring marimo UI.
"""

from dataclasses import dataclass
from typing import List, Dict
import datetime

# ═══════════════════════════════════════════════════════════════════════
# STRATEGIC LAYER
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class StrategicVision:
    """High-level goal from strategic reasoning."""
    goal: str
    context: str
    success_criteria: List[str]
    timestamp: str

def generate_vision(domain: str = "research automation") -> StrategicVision:
    """Generate strategic vision for a domain."""
    return StrategicVision(
        goal=f"Build self-improving {domain} system",
        context="Literate Garden is exploring agent stacking patterns",
        success_criteria=[
            "Agents can call other agents declaratively",
            "Execution graph is visible and debuggable",
            "Layers have clear separation of concerns",
            "System can reflect on its own architecture"
        ],
        timestamp=datetime.datetime.utcnow().isoformat()
    )

# ═══════════════════════════════════════════════════════════════════════
# TACTICAL LAYER
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class TacticalTask:
    """Mid-level task derived from strategic goal."""
    task_id: str
    description: str
    dependencies: List[str]
    estimated_complexity: str

@dataclass
class TacticalPlan:
    """Collection of tasks that implement a strategic vision."""
    vision_goal: str
    tasks: List[TacticalTask]

def break_down_vision(strategic_vision: StrategicVision) -> TacticalPlan:
    """Convert strategic vision into tactical tasks."""
    tasks = []
    for idx, criterion in enumerate(strategic_vision.success_criteria):
        task = TacticalTask(
            task_id=f"T{idx+1}",
            description=f"Implement: {criterion}",
            dependencies=[f"T{idx}" if idx > 0 else "START"],
            estimated_complexity="medium"
        )
        tasks.append(task)
    return TacticalPlan(
        vision_goal=strategic_vision.goal,
        tasks=tasks
    )

# ═══════════════════════════════════════════════════════════════════════
# EXECUTION LAYER
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class ExecutionResult:
    """Result of executing a tactical task."""
    task_id: str
    status: str
    output: Dict
    timestamp: str

def execute_task(task: TacticalTask) -> ExecutionResult:
    """Execute a single tactical task (simulated)."""
    return ExecutionResult(
        task_id=task.task_id,
        status="success",
        output={
            "action_taken": f"Implemented {task.description}",
            "artifacts": ["code_module.py", "tests.py", "docs.md"],
            "metrics": {"lines_of_code": 42, "test_coverage": 0.95}
        },
        timestamp=datetime.datetime.utcnow().isoformat()
    )

def execute_plan(plan: TacticalPlan) -> List[ExecutionResult]:
    """Execute all tasks in tactical plan."""
    return [execute_task(task) for task in plan.tasks]

# ═══════════════════════════════════════════════════════════════════════
# REFLECTION LAYER
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class Reflection:
    """Insight learned from observing agent stack execution."""
    insight_type: str
    observation: str
    recommendation: str
    confidence: float

def reflect_on_execution(vision: StrategicVision, plan: TacticalPlan,
                        results: List[ExecutionResult]) -> List[Reflection]:
    """Generate reflections by observing all layers."""
    reflections = []

    # Analyze success rate
    success_rate = sum(1 for r in results if r.status == "success") / len(results)
    reflections.append(Reflection(
        insight_type="performance",
        observation=f"Execution layer achieved {success_rate:.0%} success rate",
        recommendation="Maintain current approach" if success_rate > 0.8 else "Review error handling",
        confidence=0.9
    ))

    # Analyze alignment with vision
    reflections.append(Reflection(
        insight_type="alignment",
        observation=f"Tactical plan generated {len(plan.tasks)} tasks for vision: {vision.goal}",
        recommendation="Task granularity appears appropriate",
        confidence=0.8
    ))

    # Analyze architectural pattern
    reflections.append(Reflection(
        insight_type="architecture",
        observation="Agent stacking pattern successfully demonstrated",
        recommendation="This pattern could be generalized for other domains",
        confidence=0.95
    ))

    return reflections

# ═══════════════════════════════════════════════════════════════════════
# RUN THE AGENT STACK
# ═══════════════════════════════════════════════════════════════════════

def run_agent_stack():
    """Execute the complete agent stack and display results."""

    print("=" * 70)
    print("🏗️  AGENT STRATA EXECUTION - Infrastructure as Code")
    print("=" * 70)
    print()

    # LAYER 1: Strategic
    print("📍 STRATEGIC LAYER - Generating vision...")
    vision = generate_vision()
    print(f"   Goal: {vision.goal}")
    print(f"   Context: {vision.context}")
    print(f"   Success criteria: {len(vision.success_criteria)} defined")
    for i, criterion in enumerate(vision.success_criteria, 1):
        print(f"      {i}. {criterion}")
    print()

    # LAYER 2: Tactical (depends on Strategic output)
    print("⚙️  TACTICAL LAYER - Breaking down vision into tasks...")
    tactical_plan = break_down_vision(vision)
    print(f"   Generated {len(tactical_plan.tasks)} tasks:")
    for task in tactical_plan.tasks:
        print(f"      [{task.task_id}] {task.description}")
        print(f"          Dependencies: {', '.join(task.dependencies)}")
        print(f"          Complexity: {task.estimated_complexity}")
    print()

    # LAYER 3: Execution (depends on Tactical output)
    print("🔧 EXECUTION LAYER - Performing concrete actions...")
    execution_results = execute_plan(tactical_plan)
    print(f"   Executed {len(execution_results)} tasks:")
    for result in execution_results:
        print(f"      [{result.task_id}] Status: {result.status}")
        print(f"          Action: {result.output['action_taken']}")
        print(f"          Artifacts: {', '.join(result.output['artifacts'])}")
    print()

    # LAYER 4: Reflection (depends on ALL previous layers)
    print("🧠 REFLECTION LAYER - Analyzing execution...")
    reflections = reflect_on_execution(vision, tactical_plan, execution_results)
    print(f"   Generated {len(reflections)} insights:")
    for i, reflection in enumerate(reflections, 1):
        print(f"      {i}. [{reflection.insight_type.upper()}] (confidence: {reflection.confidence:.0%})")
        print(f"         Observation: {reflection.observation}")
        print(f"         Recommendation: {reflection.recommendation}")
    print()

    print("=" * 70)
    print("✅ AGENT STACK EXECUTION COMPLETE")
    print("=" * 70)
    print()
    print("Key Insight: Each layer called the next in sequence,")
    print("demonstrating 'call surface stacking' - the execution flow")
    print("cascaded through Strategic → Tactical → Execution → Reflection")
    print()
    print("In marimo, this would be automatic via cell dependencies!")

if __name__ == "__main__":
    run_agent_stack()
