from abc import ABC, abstractmethod


class ToolAdapter(ABC):
    @abstractmethod
    def run(self, command: str, args: list[str]):
        pass
