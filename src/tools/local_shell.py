import subprocess

from .adapter import ToolAdapter


class LocalShellAdapter(ToolAdapter):
    def run(self, command: str, args: list[str]):
        result = subprocess.run([command] + args, capture_output=True, text=True)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
        }
