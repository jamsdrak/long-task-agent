from agent.tools.adapter import ToolAdapter


class Executor:
    def __init__(self, tool_adapter: ToolAdapter):
        self.tool_adapter = tool_adapter

    def execute(self, action: str):
        return self.tool_adapter.run("echo", [action])
