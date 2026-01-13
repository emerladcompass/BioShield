#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Water Monitoring Module
"""
import random
from datetime import datetime
from pathlib import Path
import json

class WaterMonitor:
    def __init__(self, sensor_id="WATER-001"):
        self.sensor_id = sensor_id
        self.data_file = "data/processed/water_data.json"
        self.log_file = "logs/water_monitor.log"
        Path("data/processed").mkdir(parents=True, exist_ok=True)
        Path("logs").mkdir(parents=True, exist_ok=True)
        self.standards = {
            "ph": {"optimal": [6.5, 8.5], "critical": [5.5, 9.0]},
            "dissolved_oxygen": {"optimal": [6, 10], "critical": [3, 12]},
            "temperature": {"optimal": [10, 25], "critical": [5, 35]}
        }
    
    def simulate_sensor_reading(self):
        return {
            "timestamp": datetime.now().isoformat(),
            "sensor_id": self.sensor_id,
            "ph": round(random.uniform(5.5, 9.0), 2),
            "dissolved_oxygen": random.randint(2, 12),
            "temperature": random.randint(5, 35)
        }
    
    def analyze_water_health(self, data):
        analysis = {"timestamp": datetime.now().isoformat(),
                    "sensor_id": self.sensor_id,
                    "status": "NORMAL",
                    "alerts": [],
                    "scores": {}}
        
        # pH analysis
        ph = data["ph"]
        if self.standards["ph"]["optimal"][0] <= ph <= self.standards["ph"]["optimal"][1]:
            analysis["scores"]["ph"] = "OPTIMAL"
        elif self.standards["ph"]["critical"][0] <= ph <= self.standards["ph"]["critical"][1]:
            analysis["scores"]["ph"] = "ACCEPTABLE"
            analysis["alerts"].append("pH slightly off")
        else:
            analysis["scores"]["ph"] = "CRITICAL"
            analysis["alerts"].append("🚨 pH critical")
        
        # Dissolved oxygen
        do = data["dissolved_oxygen"]
        if self.standards["dissolved_oxygen"]["optimal"][0] <= do <= self.standards["dissolved_oxygen"]["optimal"][1]:
            analysis["scores"]["dissolved_oxygen"] = "OPTIMAL"
        elif self.standards["dissolved_oxygen"]["critical"][0] <= do <= self.standards["dissolved_oxygen"]["critical"][1]:
            analysis["scores"]["dissolved_oxygen"] = "ACCEPTABLE"
            analysis["alerts"].append("Dissolved oxygen slightly off")
        else:
            analysis["scores"]["dissolved_oxygen"] = "CRITICAL"
            analysis["alerts"].append("🚨 Dissolved oxygen critical")
        
        # Temperature
        temp = data["temperature"]
        if self.standards["temperature"]["optimal"][0] <= temp <= self.standards["temperature"]["optimal"][1]:
            analysis["scores"]["temperature"] = "OPTIMAL"
        elif self.standards["temperature"]["critical"][0] <= temp <= self.standards["temperature"]["critical"][1]:
            analysis["scores"]["temperature"] = "ACCEPTABLE"
            analysis["alerts"].append("Temperature slightly off")
        else:
            analysis["scores"]["temperature"] = "CRITICAL"
            analysis["alerts"].append("🚨 Temperature critical")
        
        if any("🚨" in alert for alert in analysis["alerts"]):
            analysis["status"] = "CRITICAL"
        elif analysis["alerts"]:
            analysis["status"] = "WARNING"
        else:
            analysis["status"] = "OPTIMAL"
        
        return analysis
