import json
from pathlib import Path


class PersistenceStore:
    def __init__(self, progress_path: str):
        self.progress_path = Path(progress_path)

    def save_progress(self, data):
        self.progress_path.write_text(json.dumps(data))

    def load_progress(self):
        if not self.progress_path.exists():
            return None
        return json.loads(self.progress_path.read_text())
