#!/bin/bash
# BioShield Agro-Immunity Runner
# Quick start script

echo "=========================================="
echo "    BioShield Agro-Immunity Runner       "
echo "=========================================="

cd /sdcard/download/BioShield/B_Agro_Immunity

# Check essential files
if [ ! -f "src/core/agro_immunity_engine.py" ]; then
    echo "❌ ERROR: Main engine not found"
    exit 1
fi

# Run system
echo "[+] Starting engine..."
python3 src/core/agro_immunity_engine.py $@

echo ""
echo "✅ Run completed"
echo "📁 Location: $(pwd)"
echo "🕒 Time: $(date)"
