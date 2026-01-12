#!/bin/bash
# BioShield Agro-Immunity Quick Start Script

echo "Starting BioShield Agro-Immunity System..."
echo "Date: $(date)"
echo ""

cd /sdcard/download/BioShield/B_Agro_Immunity

# Check Python
python3 --version

# Run the engine
echo ""
echo "Launching Agro-Immunity Engine..."
echo "=================================="
python3 src/core/agro_immunity_engine.py --single

echo ""
echo "BioShield session completed."
