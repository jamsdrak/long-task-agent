from .models import Phase


class Planner:
    def __init__(self, goal: str):
        self.goal = goal
        self.phases: list[Phase] = []

    def decompose(self) -> list[Phase]:
        # Replace with LLM-backed decomposition logic
        self.phases = [
            Phase(
                name="Initial Planning",
                done_criteria="Clear project structure defined",
                actions=["Define architecture", "Create directory structure"],
            )
        ]
        return self.phases

    def adapt(self, feedback: str):
        # Adapt strategy based on execution feedback
        pass
