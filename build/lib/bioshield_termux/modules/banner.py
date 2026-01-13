from datetime import datetime
import os

class Banner:
    @staticmethod
    def show_banner():
        print("\n" + "="*50)
        print("   BioShield Agro-Immunity Engine")
        print("   Version: 1.0.0")
        print("="*50)
        print(f"Author: Samir Baladi")
        print(f"Organization: Emerlad Compass 🧭")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Location: {os.getcwd()}")
