#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nutrient Monitoring Module
"""
import random
from datetime import datetime
from pathlib import Path
import json

class NutrientMonitor:
    def __init__(self):
        self.sensor_id = "NUTRIENT-001"
        self.data_file = "data/processed/nutrient_data.json"
        self.log_file = "logs/nutrient_monitor.log"
        Path("data/processed").mkdir(parents=True, exist_ok=True)
        Path("logs").mkdir(parents=True, exist_ok=True)
        self.standards = {
            "nitrogen": {"min": 15, "max": 50},
            "phosphorus": {"min": 10, "max": 40},
            "potassium": {"min": 20, "max": 60}
        }
    
    def simulate_sensor_reading(self):
        return {
            "timestamp": datetime.now().isoformat(),
            "sensor_id": self.sensor_id,
            "nitrogen": random.randint(10, 55),
            "phosphorus": random.randint(5, 45),
            "potassium": random.randint(15, 65)
        }
    
    def analyze_nutrients(self, data):
        analysis = {"timestamp": datetime.now().isoformat(),
                    "sensor_id": self.sensor_id,
                    "status": "NORMAL",
                    "alerts": [],
                    "scores": {}}
        
        for nutrient, value in data.items():
            if nutrient == "timestamp" or nutrient == "sensor_id":
                continue
            std = self.standards.get(nutrient, {"min": 0, "max": 100})
            if std["min"] <= value <= std["max"]:
                analysis["scores"][nutrient] = "NORMAL"
            elif value < std["min"]:
                analysis["scores"][nutrient] = "LOW"
                analysis["alerts"].append(f"{nutrient} LOW")
            else:
                analysis["scores"][nutrient] = "HIGH"
                analysis["alerts"].append(f"{nutrient} HIGH")
        
        if any("HIGH" in alert or "LOW" in alert for alert in analysis["alerts"]):
            analysis["status"] = "WARNING"
        return analysis
