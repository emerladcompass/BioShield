import os
import json

class ConfigManager:
    def __init__(self, base_dir, author_info):
        self.base_dir = base_dir
        self.author_info = author_info
        self.config_file = os.path.join(base_dir, "config.json")

    def create_configs(self):
        config_data = {
            "author": self.author_info,
            "version": "1.0.0",
            "last_update": None
        }
        os.makedirs(self.base_dir, exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(config_data, f, indent=2)
        print(f"[✓] Config file created at {self.config_file}")
