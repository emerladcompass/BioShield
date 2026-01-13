#!/usr/bin/env python3

from modules.directory_manager import DirectoryManager
from modules.config_manager import ConfigManager
from modules.banner import Banner
from modules.demo_monitor import DemoMonitor

class BioShieldEngine:
    def __init__(self):
        self.base_dir = "/sdcard/download/BioShield/B_Agro_Immunity"
        self.version = "1.0.0"
        self.author_info = {
            "name": "Samir Baladi",
            "organization": "Emerlad Compass 🧭",
            "email": "emerladcompass@gmail.com"
        }

        self.dir_manager = DirectoryManager(self.base_dir)
        self.config_manager = ConfigManager(self.base_dir, self.author_info)

    def run(self):
        self.dir_manager.create_directories()
        Banner.show_banner()
        self.config_manager.create_configs()
        DemoMonitor.run()
