from agent.core.executor import Executor
from agent.core.loop import MetaLoop
from agent.core.planner import Planner
from agent.persistence.store import PersistenceStore
from agent.tools.local_shell import LocalShellAdapter


class AgentOrchestrator:
    def __init__(self, config: dict):
        self.config = config

    def run(self):
        planner = Planner(self.config["goal"])
        tool_adapter = LocalShellAdapter()
        executor = Executor(tool_adapter)
        persistence = PersistenceStore(self.config["persistence"]["progress_path"])

        loop = MetaLoop(planner, executor, persistence)
        loop.run()
