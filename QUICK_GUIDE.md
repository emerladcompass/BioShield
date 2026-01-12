# 🚀 BioShield Quick Guide

## 📍 Location
```bash
cd /sdcard/download/BioShield/B_Agro_Immunity
```

🔧 Essential Commands

Run System

```bash
# Full system
python src/core/agro_immunity_engine.py

# Test only
python src/core/agro_immunity_engine.py --test

# Demo only
python src/core/agro_immunity_engine.py --demo

# Quick script
./run.sh
```

Test Modules

```bash
# Genomic module
python src/modules/genomic_integrity.py

# Network analyzer
python src/network/network_analyzer.py

# Full test suite
python test_system.py
```

📁 Key Directories

Directory Purpose Key Files
src/core/ Main engine agro_immunity_engine.py
config/ Settings settings.yaml, indicators.json
data/results/ Output *.json reports
logs/ Logs system.log, alerts.log
vault/genomic_keys/ Security Genetic fingerprints

⚙️ Configuration

Edit Settings

```bash
nano config/settings.yaml
```

View Results

```bash
# Latest report
cat data/results/demo_report.json

# System logs
tail -f logs/system.log

# Alerts
tail -f logs/alerts.log
```

🎯 Getting Started

1. Navigate to project:
   ```bash
   cd /sdcard/download/BioShield/B_Agro_Immunity
   ```
2. Test system:
   ```bash
   python src/core/agro_immunity_engine.py --test
   ```
3. Run demo:
   ```bash
   python src/core/agro_immunity_engine.py --demo
   ```
4. Check results:
   ```bash
   ls -la data/results/
   cat data/results/demo_report.json
   ```

📞 Support

· Email: emerladcompass@gmail.com
· GitHub: github.com/emerladcompass/BioShield
· Docs: docs/project_structure.md

---

For complete documentation, see docs/project_structure.md
