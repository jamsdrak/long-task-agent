# Long-Task Agent Framework

Production-grade scaffold for autonomous AI agents capable of long-horizon task execution.

## Features

- Meta-loop architecture (Plan → Execute → Test → Persist → Adapt)
- Persistent context across sessions
- Modular tool integration layer
- CI/CD ready
- Fully testable architecture

## Quick Start

```bash
git clone https://github.com/your-org/long-task-agent.git
cd long-task-agent
pip install -e .
cp .env.example .env
python scripts/run_agent.py
