
---

## `pyproject.toml`

```toml
[project]
name = "long-task-agent"
version = "1.0.0"
description = "Long-horizon autonomous AI agent framework"
authors = [{ name = "Your Name" }]
dependencies = [
    "pydantic>=2.0",
    "pyyaml",
    "loguru",
]
requires-python = ">=3.10"

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
