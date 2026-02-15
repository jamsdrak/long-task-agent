from agent.runtime.orchestrator import AgentOrchestrator
from agent.utils.config import load_config


def main():
    config = load_config("configs/agent.yaml")
    orchestrator = AgentOrchestrator(config)
    orchestrator.run()


if __name__ == "__main__":
    main()
