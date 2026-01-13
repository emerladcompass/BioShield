import os

class DirectoryManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def create_directories(self):
        os.makedirs(self.base_dir, exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "data"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "data/models"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "data/processed"), exist_ok=True)
        print(f"[✓] Directories created successfully at {self.base_dir}")
