class MetaLoop:
    def __init__(self, planner, executor, persistence):
        self.planner = planner
        self.executor = executor
        self.persistence = persistence

    def run(self):
        phases = self.planner.decompose()

        for phase in phases:
            for action in phase.actions:
                result = self.executor.execute(action)
                self.persistence.save_progress(result)
