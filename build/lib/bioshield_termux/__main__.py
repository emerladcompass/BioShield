"""
BioShield Agro-Immunity - Main Entry Point
==========================================

A Network-Based Intelligence Framework for Soil Health (2026–2046)

Author: Samir Baladi
Organization: Emerald Compass Research
Version: 3.3.0
"""

import sys
import os

# Add current directory to path for module imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main entry point for the package."""
    try:
        from .main import main as bioshield_main
        return bioshield_main()
    except ImportError as e:
        print(f"Error importing main module: {e}")
        print("Trying alternative import...")
        try:
            from main import main as bioshield_main
            return bioshield_main()
        except ImportError:
            print("Could not import main module. Please ensure the package is installed correctly.")
            return 1

if __name__ == "__main__":
    sys.exit(main())
