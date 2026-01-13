# BioShield v3.3.0 - Complete Documentation

![BioShield Banner](https://img.shields.io/badge/BioShield-v3.3.0-green?style=for-the-badge&logo=leaf)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18224754-blue?style=flat-square)](https://doi.org/10.5281/zenodo.18224754)

> **AI-powered Intelligent Soil Monitoring & Auto-Adjustment System**  
> Real-time analysis • Automatic correction • Predictive reporting

---

## 📑 Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [Installation](#installation)
- [Core Modules](#core-modules)
- [Usage Guide](#usage-guide)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Data Formats](#data-formats)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Citation](#citation)

---

## 🌱 Introduction

### What is BioShield?

BioShield v3.3.0 is an advanced, modular platform for intelligent agricultural monitoring and management. It combines real-time sensor data collection, AI-powered analysis, automatic adjustment mechanisms, and comprehensive reporting to optimize soil health and crop productivity.

### Key Features

- **🔬 Multi-Parameter Monitoring**: pH, moisture, temperature, and nutrients
- **🤖 AI Auto-Adjustment**: Intelligent real-time corrections
- **📊 Predictive Analytics**: Forecast soil health trends
- **🚨 Alert System**: Immediate notifications for critical conditions
- **📈 Live Dashboard**: Interactive visualization interface
- **📝 Automated Reporting**: Daily, weekly, and summary reports
- **🌍 Field-Ready**: Optimized for Termux and Linux environments

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8+ | 3.10+ |
| RAM | 512 MB | 1 GB+ |
| Storage | 100 MB | 500 MB+ |
| OS | Linux, Termux | Ubuntu 20.04+, Termux |

---

## 🏗️ Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────┐
│                    BioShield System                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   Sensors    │  │  AI Engine   │  │  Dashboard   │ │
│  │              │  │              │  │              │ │
│  │ • pH         │─▶│ • Analyzer   │─▶│ • Live View  │ │
│  │ • Moisture   │  │ • Predictor  │  │ • Charts     │ │
│  │ • Temp       │  │ • Adjuster   │  │ • Alerts     │ │
│  │ • Nutrients  │  │              │  │              │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│         │                 │                  │         │
│         └─────────────────┴──────────────────┘         │
│                           │                            │
│                  ┌────────▼────────┐                   │
│                  │  Data Storage   │                   │
│                  │  & Reporting    │                   │
│                  └─────────────────┘                   │
└─────────────────────────────────────────────────────────┘
```

### Directory Structure

```
BioShield/
├── src/                          # Source code
│   ├── main.py                   # CLI entry point
│   ├── final_system.py           # Integrated system
│   ├── core/                     # Core engine
│   │   ├── __init__.py
│   │   └── engine.py
│   └── modules/                  # Functional modules
│       ├── __init__.py
│       ├── soil_monitor.py       # Soil sensing
│       ├── water_monitor.py      # Water quality
│       ├── nutrient_monitor.py   # Nutrient tracking
│       ├── auto_adjuster.py      # Auto-correction
│       ├── ai_predictor.py       # ML predictions
│       ├── report_generator.py   # Report creation
│       ├── live_dashboard.py     # Visualization
│       ├── alert_manager.py      # Alert system
│       ├── banner.py             # UI banner
│       ├── demo_monitor.py       # Demo mode
│       └── directory_manager.py  # File management
├── config/                       # Configuration files
│   └── config.json
├── data/                         # Data storage
│   ├── raw/                      # Raw sensor data
│   ├── processed/                # Processed data
│   └── archive/                  # Historical data
├── logs/                         # System logs
├── reports/                      # Generated reports
│   ├── daily/
│   ├── weekly/
│   └── summary/
├── tests/                        # Unit tests
├── vault/                        # Secure storage
├── docs/                         # Documentation
├── README.md
├── LICENSE
├── requirements.txt
├── CHANGELOG.md
└── CONTRIBUTING.md
```

### Data Flow

```
┌─────────────┐
│   Sensors   │
└──────┬──────┘
       │ Raw Data
       ▼
┌─────────────┐
│  Monitor    │ ◀─── config.json
└──────┬──────┘
       │ Validated Data
       ▼
┌─────────────┐
│  Analyzer   │
└──────┬──────┘
       │ Analysis Results
       ├──────────────┬──────────────┐
       ▼              ▼              ▼
┌──────────┐   ┌──────────┐   ┌──────────┐
│ Adjuster │   │ Predictor│   │  Alerts  │
└────┬─────┘   └────┬─────┘   └────┬─────┘
     │              │              │
     └──────────────┴──────────────┘
                    │
                    ▼
            ┌───────────────┐
            │   Dashboard   │
            │   & Reports   │
            └───────────────┘
```

---

## 📥 Installation

### Method 1: Quick Install (Recommended)

```bash
# Clone repository
git clone https://github.com/emerladcompass/BioShield.git
cd BioShield

# Install dependencies
pip install -r requirements.txt

# Run system test
python src/main.py --mode demo
```

### Method 2: From Zenodo Archive

```bash
# Download from Zenodo
wget https://zenodo.org/record/18224754/files/BioShield-v3.3.0.zip

# Extract
unzip BioShield-v3.3.0.zip
cd BioShield-v3.3.0

# Install
pip install -r requirements.txt
```

### Method 3: Development Install

```bash
# Clone with development branch
git clone -b develop https://github.com/emerladcompass/BioShield.git
cd BioShield

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt
```

### Termux Installation

```bash
# Update packages
pkg update && pkg upgrade

# Install Python
pkg install python

# Install git
pkg install git

# Clone and install
git clone https://github.com/emerladcompass/BioShield.git
cd BioShield
pip install -r requirements.txt
```

---

## 🔬 Core Modules

### 1. Soil Monitor (`soil_monitor.py`)

**Purpose**: Real-time soil parameter monitoring

**Parameters Monitored**:
- pH level (0-14 scale)
- Moisture content (0-100%)
- Temperature (°C)
- Soil health status

**Key Methods**:

```python
from modules.soil_monitor import SoilMonitor

monitor = SoilMonitor()

# Read sensor data
soil_data = monitor.simulate_sensor_reading()
# Returns: {'ph': 6.91, 'moisture': 47, 'temperature': 28}

# Analyze soil health
analysis = monitor.analyze_soil_health(soil_data)
# Returns: {'status': 'GOOD', 'alerts': [], 'recommendations': [...]}

# Save data
monitor.save_data(soil_data, analysis)
```

**Configuration**:
```json
{
  "soil": {
    "ph_range": [6.0, 7.5],
    "moisture_min": 30,
    "moisture_max": 70,
    "temp_optimal": [18, 28]
  }
}
```

---

### 2. Auto Adjuster (`auto_adjuster.py`)

**Purpose**: Automatic correction of soil conditions

**Features**:
- Real-time pH adjustment
- Automatic irrigation control
- Temperature regulation recommendations
- Adaptive correction algorithms

**Key Methods**:

```python
from modules.auto_adjuster import SoilAutoAdjuster

adjuster = SoilAutoAdjuster()

# Run full adjustment cycle
analysis = adjuster.run_auto_adjustment_cycle(soil_data)
# Returns: {
#   'status': 'ADJUSTED',
#   'actions_taken': ['Added lime for pH', 'Increased irrigation'],
#   'new_values': {...}
# }

# Individual adjustments
adjuster.adjust_ph(current_ph=6.2, target_ph=7.0)
adjuster.adjust_moisture(current=35, target=50)
```

**Adjustment Rules**:

| Parameter | Condition | Action |
|-----------|-----------|--------|
| pH < 6.0 | Too acidic | Add lime |
| pH > 7.5 | Too alkaline | Add sulfur |
| Moisture < 30% | Too dry | Increase irrigation |
| Moisture > 70% | Too wet | Reduce irrigation |
| Temp > 30°C | Too hot | Increase shading |

---

### 3. Water Monitor (`water_monitor.py`)

**Purpose**: Water quality and availability tracking

**Parameters**:
- Water pH
- Dissolved oxygen
- Conductivity
- Turbidity

**Usage**:

```python
from modules.water_monitor import WaterMonitor

water_monitor = WaterMonitor()
water_data = water_monitor.simulate_sensor_reading()
water_analysis = water_monitor.analyze_water_quality(water_data)
```

---

### 4. Nutrient Monitor (`nutrient_monitor.py`)

**Purpose**: Track essential soil nutrients

**Nutrients Tracked**:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Micronutrients

**Usage**:

```python
from modules.nutrient_monitor import NutrientMonitor

nutrient_monitor = NutrientMonitor()
nutrient_data = nutrient_monitor.simulate_sensor_reading()
nutrient_analysis = nutrient_monitor.analyze_nutrients(nutrient_data)
```

---

### 5. AI Predictor (`ai_predictor.py`)

**Purpose**: Predictive analytics for soil health

**Features**:
- 7-day health forecasting
- Trend analysis
- Anomaly detection
- Risk assessment

**Usage**:

```python
from modules.ai_predictor import AIPredictor

predictor = AIPredictor()

# Predict future trends
forecast = predictor.predict_trends(historical_data)
# Returns: {
#   'next_7_days': [...],
#   'confidence': 0.85,
#   'risk_level': 'LOW'
# }

# Detect anomalies
anomalies = predictor.detect_anomalies(current_data)
```

---

### 6. Report Generator (`report_generator.py`)

**Purpose**: Automated report creation

**Report Types**:
- Daily reports
- Weekly summaries
- Monthly analytics
- Custom period reports

**Usage**:

```python
from modules.report_generator import ReportGenerator
from pathlib import Path

report_gen = ReportGenerator()

# Generate daily report
daily_data = [...]  # List of cycle data
report = report_gen.generate_daily_report(daily_data)

# Save report
report_file = Path("reports/daily/report_2026-01-12.txt")
report_gen.save_report(report, report_file)
```

**Report Structure**:
```
Daily Report Summary
============================================================
Report ID: DAILY-2026-01-12
Generated At: 2026-01-12T15:35:59
System Version: B_Agro_Immunity v3.0
============================================================

📊 Data Per Cycle:
[Cycle-by-cycle data]

📋 Daily Summary:
- Total Samples
- Total Alerts
- Critical Alerts
- Soil Health Status
- Key Findings
- Recommendations
- Next Steps
```

---

### 7. Live Dashboard (`live_dashboard.py`)

**Purpose**: Real-time visualization interface

**Features**:
- Live data updates
- Interactive charts
- Alert notifications
- Historical trends

**Usage**:

```python
from modules.live_dashboard import LiveDashboard

dashboard = LiveDashboard()
dashboard.launch()  # Opens web interface on localhost:8050
```

---

### 8. Alert Manager (`alert_manager.py`)

**Purpose**: Real-time alert system

**Alert Levels**:
- 🟢 **INFO**: Normal conditions
- 🟡 **WARNING**: Attention needed
- 🔴 **CRITICAL**: Immediate action required

**Usage**:

```python
from modules.alert_manager import AlertManager

alert_mgr = AlertManager()

# Check conditions and send alerts
alert_mgr.check_and_alert(soil_data, analysis)

# Manual alert
alert_mgr.send_alert(
    level="CRITICAL",
    message="pH level dangerously low",
    data=soil_data
)
```

---

## 📖 Usage Guide

### Basic Usage

#### 1. Demo Mode (Quick Test)

```bash
python src/main.py --mode demo
```

**Output**:
```
╔══════════════════════════════════════════════════════════╗
║        🌱 BioShield v3.3.0 - Agro-Systemic System 🌱    ║
╚══════════════════════════════════════════════════════════╝

[*] Running Demo Monitoring Cycle...

🌀 Cycle 1/3
  pH: 6.85 ✓
  Moisture: 45% ✓
  Temperature: 24°C ✓
  Status: HEALTHY
```

#### 2. Full Monitoring

```bash
python src/main.py --mode all
```

**Features**:
- Monitors all sensors
- Runs auto-adjustment
- Generates reports
- Updates dashboard

#### 3. Auto-Adjustment Only

```bash
python src/main.py --mode auto
```

**Use Case**: When you have external sensors but want BioShield's adjustment logic

---

### Advanced Usage

#### Custom Cycle Duration

```python
from src.modules.soil_monitor import SoilMonitor
from src.modules.auto_adjuster import SoilAutoAdjuster
import time

monitor = SoilMonitor()
adjuster = SoilAutoAdjuster()

# Run for 10 cycles with 5-second intervals
for i in range(10):
    soil_data = monitor.simulate_sensor_reading()
    analysis = adjuster.run_auto_adjustment_cycle(soil_data)
    print(f"Cycle {i+1}: {analysis['status']}")
    time.sleep(5)
```

#### Integration with Real Sensors

```python
from src.modules.soil_monitor import SoilMonitor

class RealSensorMonitor(SoilMonitor):
    def read_real_sensor(self):
        # Replace with actual sensor reading code
        import board
        import adafruit_dht
        
        dht_sensor = adafruit_dht.DHT22(board.D4)
        
        return {
            'ph': self.read_ph_sensor(),
            'moisture': self.read_moisture_sensor(),
            'temperature': dht_sensor.temperature
        }

monitor = RealSensorMonitor()
data = monitor.read_real_sensor()
```

#### Batch Processing

```python
from pathlib import Path
from src.modules.report_generator import ReportGenerator

report_gen = ReportGenerator()

# Process multiple days of data
data_dir = Path("data/raw")
for data_file in data_dir.glob("*.json"):
    with open(data_file) as f:
        daily_data = json.load(f)
    
    report = report_gen.generate_daily_report(daily_data)
    report_gen.save_report(report, f"reports/batch/{data_file.stem}.txt")
```

---

## 🔌 API Reference

### SoilMonitor Class

```python
class SoilMonitor:
    """Monitor soil parameters in real-time"""
    
    def __init__(self, config_path: str = "config/config.json"):
        """Initialize monitor with configuration"""
        pass
    
    def simulate_sensor_reading(self) -> dict:
        """
        Simulate sensor reading (replace with real sensors)
        
        Returns:
            dict: {'ph': float, 'moisture': int, 'temperature': float}
        """
        pass
    
    def analyze_soil_health(self, soil_data: dict) -> dict:
        """
        Analyze soil health from sensor data
        
        Args:
            soil_data: Dictionary containing sensor readings
            
        Returns:
            dict: Analysis results with status and recommendations
        """
        pass
    
    def save_data(self, soil_data: dict, analysis: dict) -> None:
        """Save data to storage"""
        pass
```

### SoilAutoAdjuster Class

```python
class SoilAutoAdjuster:
    """Automatic soil condition adjustment"""
    
    def __init__(self):
        """Initialize adjuster"""
        pass
    
    def run_auto_adjustment_cycle(self, soil_data: dict) -> dict:
        """
        Run complete adjustment cycle
        
        Args:
            soil_data: Current soil readings
            
        Returns:
            dict: Adjustment results and actions taken
        """
        pass
    
    def adjust_ph(self, current_ph: float, target_ph: float) -> str:
        """Adjust pH level"""
        pass
    
    def adjust_moisture(self, current: int, target: int) -> str:
        """Adjust moisture level"""
        pass
```

### ReportGenerator Class

```python
class ReportGenerator:
    """Generate automated reports"""
    
    def __init__(self):
        """Initialize generator"""
        pass
    
    def generate_daily_report(self, daily_data: list) -> str:
        """
        Generate daily summary report
        
        Args:
            daily_data: List of cycle data dictionaries
            
        Returns:
            str: Formatted report text
        """
        pass
    
    def save_report(self, report: str, filepath: Path) -> None:
        """Save report to file"""
        pass
```

---

## ⚙️ Configuration

### config.json Structure

```json
{
  "system": {
    "version": "3.3.0",
    "name": "BioShield",
    "mode": "production"
  },
  "soil": {
    "ph_range": [6.0, 7.5],
    "ph_optimal": 7.0,
    "moisture_min": 30,
    "moisture_max": 70,
    "moisture_optimal": 50,
    "temp_min": 18,
    "temp_max": 28,
    "temp_optimal": 23
  },
  "water": {
    "ph_range": [6.5, 8.0],
    "do_min": 5.0,
    "conductivity_max": 2000
  },
  "nutrients": {
    "nitrogen_range": [20, 40],
    "phosphorus_range": [10, 30],
    "potassium_range": [15, 35]
  },
  "monitoring": {
    "cycle_interval": 60,
    "cycles_per_day": 5,
    "alert_threshold": "WARNING"
  },
  "reporting": {
    "daily_enabled": true,
    "weekly_enabled": true,
    "format": "txt",
    "include_charts": false
  },
  "alerts": {
    "email_enabled": false,
    "sms_enabled": false,
    "log_enabled": true
  }
}
```

### Environment Variables

```bash
# .env file
BIOSHIELD_MODE=production
BIOSHIELD_CONFIG=config/config.json
BIOSHIELD_DATA_DIR=data
BIOSHIELD_LOG_LEVEL=INFO
BIOSHIELD_ALERT_EMAIL=alerts@example.com
```

---

## 📊 Data Formats

### Sensor Data Format

```json
{
  "timestamp": "2026-01-12T15:35:59.576983",
  "sensor_id": "SOIL_001",
  "readings": {
    "ph": 6.91,
    "moisture": 47,
    "temperature": 28.0,
    "conductivity": 1200
  },
  "location": {
    "latitude": 31.7917,
    "longitude": -7.0926,
    "zone": "Field_A"
  }
}
```

### Analysis Result Format

```json
{
  "timestamp": "2026-01-12T15:35:59.576983",
  "status": "NEEDS_ATTENTION",
  "health_score": 72,
  "alerts": [
    {
      "level": "WARNING",
      "parameter": "moisture",
      "message": "Moisture below optimal range",
      "value": 34,
      "threshold": 40
    }
  ],
  "recommendations": [
    "Increase irrigation by 20%",
    "Monitor moisture levels closely"
  ]
}
```

---

## 💡 Examples

### Example 1: Basic Monitoring Script

```python
#!/usr/bin/env python3
from src.modules.soil_monitor import SoilMonitor

def main():
    monitor = SoilMonitor()
    
    # Single reading
    data = monitor.simulate_sensor_reading()
    analysis = monitor.analyze_soil_health(data)
    
    print(f"pH: {data['ph']}")
    print(f"Status: {analysis['status']}")
    
    if analysis['alerts']:
        print("⚠️ Alerts:")
        for alert in analysis['alerts']:
            print(f"  - {alert}")

if __name__ == "__main__":
    main()
```

### Example 2: Continuous Monitoring with Auto-Adjustment

```python
#!/usr/bin/env python3
import time
from src.modules.soil_monitor import SoilMonitor
from src.modules.auto_adjuster import SoilAutoAdjuster

def continuous_monitoring(duration_hours=24, interval_minutes=30):
    monitor = SoilMonitor()
    adjuster = SoilAutoAdjuster()
    
    cycles = (duration_hours * 60) // interval_minutes
    
    for i in range(cycles):
        print(f"\n{'='*50}")
        print(f"Cycle {i+1}/{cycles}")
        
        # Read sensors
        soil_data = monitor.simulate_sensor_reading()
        
        # Run auto-adjustment
        result = adjuster.run_auto_adjustment_cycle(soil_data)
        
        print(f"Status: {result['status']}")
        if result.get('actions_taken'):
            print("Actions:")
            for action in result['actions_taken']:
                print(f"  ✓ {action}")
        
        # Wait for next cycle
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    continuous_monitoring(duration_hours=24, interval_minutes=30)
```

### Example 3: Generate Weekly Summary

```python
#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timedelta
from src.modules.report_generator import ReportGenerator
import json

def generate_weekly_summary():
    report_gen = ReportGenerator()
    
    # Collect data from past 7 days
    weekly_data = []
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        
        data_file = Path(f"data/processed/{date_str}.json")
        if data_file.exists():
            with open(data_file) as f:
                daily_data = json.load(f)
                weekly_data.extend(daily_data)
    
    # Generate report
    report = report_gen.generate_weekly_report(weekly_data)
    
    # Save
    report_file = Path(f"reports/weekly/summary_{datetime.now().strftime('%Y-W%W')}.txt")
    report_gen.save_report(report, report_file)
    
    print(f"✅ Weekly summary saved: {report_file}")

if __name__ == "__main__":
    generate_weekly_summary()
```

---

## 🔧 Troubleshooting

### Common Issues

#### Issue 1: Module Import Error

**Error**:
```
ModuleNotFoundError: No module named 'modules'
```

**Solution**:
```bash
# Ensure you're in the project root
cd BioShield

# Add src to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Or use the correct import
python -m src.main
```

#### Issue 2: Config File Not Found

**Error**:
```
FileNotFoundError: [Errno 2] No such file or directory: 'config/config.json'
```

**Solution**:
```bash
# Create default config
mkdir -p config
cp config/config.example.json config/config.json

# Or specify path
python src/main.py --config /path/to/config.json
```

#### Issue 3: Permission Denied (Termux)

**Error**:
```
PermissionError: [Errno 13] Permission denied: 'reports/daily'
```

**Solution**:
```bash
# Grant storage permissions
termux-setup-storage

# Create directories manually
mkdir -p reports/daily reports/weekly logs data
chmod -R 755 reports logs data
```

#### Issue 4: Sensor Simulation Values Out of Range

**Problem**: Simulated values unrealistic

**Solution**: Adjust ranges in `config.json`:
```json
{
  "simulation": {
    "ph_range": [6.0, 7.5],
    "moisture_range": [30, 70],
    "temp_range": [18, 28]
  }
}
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/BioShield.git
cd BioShield

# Create branch
git checkout -b feature/your-feature

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Make changes and commit
git add .
git commit -m "Add: your feature description"
git push origin feature/your-feature
```

### Code Style

- Follow PEP 8
- Use type hints
- Document all functions
- Write unit tests
- Update CHANGELOG.md

---

## 📚 Citation

If you use BioShield in your research, please cite:

```bibtex
@software{baladi2026bioshield,
  author = {Baladi, Samir},
  title = {{BioShield v3.3.0: Intelligent Soil Monitoring & Auto-Adjustment System}},
  year = 2026,
  publisher = {Zenodo},
  version = {3.3.0},
  doi = {10.5281/zenodo.18224754},
  url = {https://doi.org/10.5281/zenodo.18224754}
}
```

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/emerladcompass/BioShield/issues)
- **Email**: emerladcompass@gmail.com
- **Discussions**: [GitHub Discussions](https://github.com/emerladcompass/BioShield/discussions)

---

## 📄 License

BioShield is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

---

## 🙏 Acknowledgments

- Emerlad Compass team
- Open source community
- Agricultural research partners

---

<div align="center">

---

**BioShield v3.3.0** | Released January 2026 | MIT License

*"AI-powered soil monitoring. Real-time alerts. Predictive insights."*

Copyright © 2026 Samir Baladi | MIT License

[⬆ Back to Top](#bioshield-v3.3.0-documentation)

---
