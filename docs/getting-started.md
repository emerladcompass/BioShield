
---

layout: default
title: Getting Started
permalink: /getting-started

---

Getting Started

Installation

1. Clone the repository:

```bash
git clone https://github.com/emerladcompass/BioShield.git
cd BioShield
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

1. Run the system:

```bash
# Demo mode
python src/main.py --mode demo

# Live monitoring
python src/main.py --mode live

# Complete system
python src/main.py --mode all
```

Configuration

Edit config/config.json to adjust system parameters:

```json
{
  "system": {
    "name": "BioShield",
    "version": "3.3.0",
    "auto_adjust": true
  },
  "soil": {
    "ph_target": 6.8,
    "moisture_target": 65
  }
}
```

Quick Commands

Command Description
python src/main.py --mode demo Run demonstration
python src/main.py --mode live Live monitoring
python src/main.py --mode all Complete system
python src/run_auto_adjust.py Auto-adjustment only

