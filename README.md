# Long-Task Agent Framework

Production-grade scaffold for autonomous AI agents capable of long-horizon task execution.
Base on GLM5, Gameboy and Long-Task Era
https://blog.e01.ai/glm5-gameboy-and-long-task-era-64db7074a026

## Features

- Meta-loop architecture (Plan → Execute → Test → Persist → Adapt)
- Persistent context across sessions
- Modular tool integration layer
- CI/CD ready
- Fully testable architecture

## Quick Start

```bash
git clone https://github.com/jamsdrak/long-task-agent.git
cd long-task-agent
pip install -e .
cp .env.example .env
python scripts/run_agent.py


