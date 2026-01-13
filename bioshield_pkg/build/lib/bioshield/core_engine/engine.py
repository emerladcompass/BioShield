#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from modules.soil_monitor import SoilMonitor
from modules.water_monitor import WaterMonitor
from modules.nutrient_monitor import NutrientMonitor
from modules.banner import Banner
from modules.demo_monitor import DemoMonitor

class Engine:
    def __init__(self):
        self.banner = Banner()
        self.soil_monitor = SoilMonitor()
        self.water_monitor = WaterMonitor()
        self.nutrient_monitor = NutrientMonitor()
        self.demo_monitor = DemoMonitor()

    def run_demo(self):
        self.banner.show_banner()
        self.demo_monitor.run_cycle()

    def run_full_monitoring(self):
        self.banner.show_banner()
        print("\n[*] بدء Full Monitoring لجميع المستشعرات...\n")
        
        soil_data = self.soil_monitor.simulate_sensor_reading()
        soil_analysis = self.soil_monitor.analyze_soil_health(soil_data)
        self.soil_monitor.save_data(soil_data, soil_analysis)
        print(f"🌱 Soil status: {soil_analysis['status']}")

        water_data = self.water_monitor.simulate_sensor_reading()
        water_analysis = self.water_monitor.analyze_water_quality(water_data)
        self.water_monitor.save_data(water_data, water_analysis)
        print(f"💧 Water status: {water_analysis['status']}")

        nutrient_data = self.nutrient_monitor.simulate_sensor_reading()
        nutrient_analysis = self.nutrient_monitor.analyze_nutrients(nutrient_data)
        self.nutrient_monitor.save_data(nutrient_data, nutrient_analysis)
        print(f"🌾 Nutrients status: {nutrient_analysis['status']}")

        print("\n✅ Full Monitoring مكتمل لجميع المستشعرات!")
