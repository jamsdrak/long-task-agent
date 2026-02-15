from typing import List

from pydantic import BaseModel


class Phase(BaseModel):
    name: str
    done_criteria: str
    actions: List[str]


class AgentGoal(BaseModel):
    goal: str
    phases: List[Phase]
