# 🏗️ Project Structure Documentation
## 📁 BioShield Agro-Immunity System Architecture

**Author:** Samir Baladi  
**Organization:** Emerlad Compass 🧭  
**Version:** 1.0.0  
**Last Updated:** 2026-01-11  

---

## 📍 Project Location
```bash
/sdcard/download/BioShield/B_Agro_Immunity/
```

---

🗂️ Complete Directory Structure

📊 Visual Overview

```
BioShield/B_Agro_Immunity/
├── 📂 src/                    # Source Code (The Brain)
│   ├── 📂 core/              # Core Engine
│   │   └── 🐍 agro_immunity_engine.py
│   ├── 📂 modules/           # Specialized Modules
│   │   └── 🧬 genomic_integrity.py
│   ├── 📂 network/           # Network Analysis
│   │   └── 🌐 network_analyzer.py
│   └── 📂 utils/             # Utilities (Future)
│
├── ⚙️ config/                # Configuration Files
│   ├── ⚙️ settings.yaml
│   ├── 📊 indicators.json
│   └── 🔗 network_params.json
│
├── 💾 data/                  # Data Storage
│   ├── 📥 raw/              # Raw Data
│   ├── 🔧 processed/        # Processed Data
│   ├── 🤖 models/          # AI Models (Future)
│   └── 📊 results/         # Analysis Results
│       ├── initial_test.json
│       └── demo_report.json
│
├── 🔐 vault/                # Secure Storage
│   ├── 🧬 genomic_keys/    # Genetic Fingerprints
│   ├── 🌱 soil_profiles/   # Soil Profiles
│   └── 🔑 crypto_vaults/   # Encryption (Future)
│
├── 📚 docs/                 # Documentation
│   ├── 📖 theory/          # Theoretical Papers
│   ├── 📋 protocols/       # Operational Protocols
│   ├── 🔌 api/             # API Documentation (Future)
│   └── 📐 diagrams/        # Diagrams (Future)
│
├── 📝 logs/                # System Logs
│   ├── 📄 system.log
│   ├── ⚠️ alerts.log
│   └── 📈 performance.log
│
├── 🧪 tests/               # Testing Framework
│   └── test_system.py
│
└── 📄 Root Files
    ├── 📋 README.md
    ├── ⚖️ LICENSE
    ├── 📦 requirements.txt
    ├── 🚫 .gitignore
    └── 🚀 run.sh
```

---

🔍 Detailed Directory Explanation

1. 📂 src/ - Source Code Directory

Purpose: Contains all Python source code files.

📁 src/core/ - Core Engine

Files:

· agro_immunity_engine.py - Main System Engine
  · Initializes the system
  · Calculates System Vulnerability Index (SVI)
  · Manages monitoring cycles
  · Generates reports and alerts

📁 src/modules/ - Specialized Modules

Files:

· genomic_integrity.py - Genetic Protection Module
  · Creates genetic fingerprints for crops
  · Detects genetic contamination
  · Monitors genetic drift
  · Stores profiles in secure vault

📁 src/network/ - Network Analysis

Files:

· network_analyzer.py - Network Analysis Engine
  · Adapted from HydroNet framework
  · Calculates transfer entropy
  · Detects network instability
  · Predicts collapse risk

📁 src/utils/ - Utilities (Future Expansion)

Planned Files:

· data_cleaner.py - Data preprocessing
· visualization.py - Chart generation
· encryption.py - Security utilities
· logger.py - Advanced logging

---

2. ⚙️ config/ - Configuration Directory

Purpose: Stores all system configuration files.

📄 settings.yaml - System Settings

```yaml
system:
  name: "BioShield Agro-Immunity"
  version: "1.0.0"
  mode: "constitutive_immunity"

monitoring:
  prediction_window: 8        # months
  update_frequency: "daily"

thresholds:
  accelerator_mode: 0.70      # 🟢 Green
  stable_mode: 0.55           # 🟡 Yellow
  drain_mode: 0.40            # 🟠 Orange
  critical_mode: 0.30         # 🔴 Red
```

📄 indicators.json - 12 Indicators Framework

Contains 12 indicators across 4 domains:

1. Soil Health (B1-B3)
2. Water Link (B4-B6)
3. Genomic Integrity (B7-B9)
4. Ecological Network (B10-B12)

📄 network_params.json - Network Parameters

Sigma logic settings and prediction parameters.

---

3. 💾 data/ - Data Storage Directory

Purpose: Hierarchical data storage system.

📁 data/raw/ - Raw Data

Future Contents:

· Sensor readings (.csv)
· Laboratory measurements (.json)
· Field observations (.txt)
· Survey data (.xlsx)

📁 data/processed/ - Cleaned Data

Processing Pipeline:

1. Data cleaning
2. Normalization
3. Aggregation
4. Transformation

📁 data/models/ - AI Models

Future Models:

· Random Forest (.pkl)
· Neural Networks (.h5)
· SVM Models (.joblib)
· Clustering Models (.pkl)

📁 data/results/ - Analysis Results

Current Files:

· initial_test.json - First system test results
· demo_report.json - Demo monitoring results

Example Report Structure:

```json
{
  "author": "Samir Baladi",
  "organization": "Emerlad Compass 🧭",
  "timestamp": "2026-01-11T12:34:56",
  "svi_score": 0.682,
  "status": "STABLE",
  "indicators": {
    "B1": 0.78, "B2": 0.65, ... "B12": 0.55
  }
}
```

---

4. 🔐 vault/ - Secure Storage Directory

Purpose: Protected storage for sensitive information.

📁 vault/genomic_keys/ - Genetic Fingerprints

Files: {Crop_Name}.json

```json
{
  "crop_name": "Wheat_Native",
  "genetic_hash": "ca4999fce92c60aa...",
  "purity_score": 0.833,
  "protected": true
}
```

📁 vault/soil_profiles/ - Soil Profiles

Stores: Chemical composition, microbiome, physical properties.

📁 vault/crypto_vaults/ - Encryption Storage

Future: Private keys, certificates, encrypted data.

---

5. 📚 docs/ - Documentation Directory

Purpose: Comprehensive project documentation.

📁 docs/theory/ - Theoretical Framework

Files:

· constitutive_immunity.md - Core theory
· sigma_logic_adaptation.md - Sigma logic
· 12_indicators_framework.md - Indicator system

📁 docs/protocols/ - Operational Protocols

Files:

· early_warning.md - Early warning procedures
· intervention_tiers.md - Intervention levels
· genomic_integrity.md - Genetic protection protocols

📁 docs/api/ - API Documentation

Future: REST API documentation, SDK guides.

📁 docs/diagrams/ - Visual Documentation

Future: System architecture diagrams, data flow charts.

---

6. 📝 logs/ - Logging Directory

Purpose: System activity and error tracking.

📄 logs/system.log - System Events

Format:

```
[YYYY-MM-DD HH:MM:SS] Event description
```

📄 logs/alerts.log - Alert Records

Example:

```
[2026-01-11 12:40:00] WARNING: System in DRAIN mode
[2026-01-11 12:45:00] CRITICAL: Genetic contamination detected
```

📄 logs/performance.log - Performance Metrics

Data: Processing time, memory usage, CPU utilization.

---

7. 🧪 tests/ - Testing Directory

Purpose: Quality assurance and validation.

🐍 test_system.py - Comprehensive Test Suite

Tests:

· Module imports
· File system structure
· Main engine functionality
· Genomic module
· Network analyzer

Run: python test_system.py

---

8. 📄 Root Files - Project Management

📋 README.md - Project Overview

Main documentation with:

· Author information
· Quick start guide
· System principles
· Getting started checklist

⚖️ LICENSE - MIT License

Open-source license terms.

📦 requirements.txt - Python Dependencies

```txt
numpy>=1.21.0
pandas>=1.3.0
networkx>=2.6.0
pyyaml>=5.4.0
```

🚫 .gitignore - Version Control Exclusions

Prevents sensitive data from being tracked by Git.

🚀 run.sh - Quick Start Script

```bash
#!/bin/bash
cd /sdcard/download/BioShield/B_Agro_Immunity
python src/core/agro_immunity_engine.py $@
```

---

🔄 Data Flow Between Directories

🎯 Typical Workflow:

```
config/ → src/ → data/ → vault/ → logs/
   ↓        ↓        ↓        ↓       ↓
Settings → Processing → Storage → Security → Logging
```

📊 Example: Genetic Analysis Flow

1. Config: Load settings from config/settings.yaml
2. Processing: Analyze in src/modules/genomic_integrity.py
3. Storage: Save results to data/results/
4. Security: Store fingerprint in vault/genomic_keys/
5. Logging: Record activity in logs/system.log

---

🛠️ Development Guidelines

For Developers:

```bash
# 1. Modify configuration
cd config/
nano settings.yaml

# 2. Develop code
cd ../src/core/
nano agro_immunity_engine.py

# 3. Test changes
cd ../../tests/
python test_system.py

# 4. Check logs
cd ../logs/
tail -f system.log
```

For Researchers:

```bash
# 1. Read theory
cd docs/theory/
cat constitutive_immunity.md

# 2. Run experiments
cd ../../src/modules/
python genomic_integrity.py

# 3. Analyze results
cd ../../data/results/
cat *.json
```

For Users:

```bash
# 1. Quick start
./run.sh

# 2. Check status
cd data/results/
ls -la *.json

# 3. Monitor alerts
cd ../logs/
tail -f alerts.log
```

---

📈 Statistics & Metrics

File Count by Type:

```bash
# Python files
find . -name "*.py" | wc -l

# JSON files
find . -name "*.json" | wc -l

# YAML files
find . -name "*.yaml" -o -name "*.yml" | wc -l

# Documentation files
find . -name "*.md" | wc -l
```

Directory Sizes:

```bash
# Check sizes
du -sh */
```

---

🔮 Future Expansion Plans

New Directories to Add:

```
backups/           # Backup storage
exports/           # Data export formats
imports/           # Data import handlers
plugins/           # Plugin system
translations/      # Multi-language support
web/               # Web interface
mobile/            # Mobile application
```

New Module Files:

```
src/utils/visualization.py    # Data visualization
src/api/rest_server.py        # REST API server
src/iot/sensor_connector.py   # IoT sensor integration
src/ai/predictive_models.py   # Predictive analytics
```

---

🎯 Quick Reference

Essential Commands:

```bash
# Run main system
python src/core/agro_immunity_engine.py

# Test specific module
python src/modules/genomic_integrity.py

# Comprehensive test
python test_system.py

# Quick start
./run.sh
```

Key Configuration Files:

1. config/settings.yaml - Main settings
2. config/indicators.json - 12 indicators
3. config/network_params.json - Network parameters

Important Data Locations:

1. data/results/ - Analysis results
2. vault/genomic_keys/ - Genetic fingerprints
3. logs/ - System logs

---

📞 Support & Contact

Author: Samir Baladi
Organization: Emerlad Compass 🧭
Email: emerladcompass@gmail.com
GitHub: https://github.com/emerladcompass/BioShield
Dashboard: bioshield-b1.netlify.app

---

This document was automatically generated from the BioShield Agro-Immunity project structure.
Last Updated: 2026-01-11
