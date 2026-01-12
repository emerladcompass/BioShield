#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تشغيل نظام التعديل التلقائي
"""
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from modules.auto_adjuster import SoilAutoAdjuster
from modules.soil_monitor import SoilMonitor

print("\n" + "="*60)
print("🤖 تشغيل نظام التعديل التلقائي للتربة")
print("="*60)

# إنشاء المراقب والمعدل
soil_monitor = SoilMonitor()
adjuster = SoilAutoAdjuster()

# تشغيل 3 دورات
for i in range(1, 4):
    print(f"\n🌀 الدورة رقم {i}")
    print("-"*40)
    
    # محاكاة قراءة التربة
    soil_data = soil_monitor.simulate_sensor_reading()
    print(f"📡 قراءة التربة:")
    print(f"   - pH: {soil_data['ph']}")
    print(f"   - الرطوبة: {soil_data['moisture']}%")
    print(f"   - الحرارة: {soil_data['temperature']}°C")
    
    # التحليل والتعديل
    adjuster.run_auto_adjustment_cycle(soil_data)
    
    if i < 3:
        import time
        print("\n⏳ انتظار 3 ثواني للدورة التالية...")
        time.sleep(3)

print("\n" + "="*60)
print("✅ اكتمل نظام التعديل التلقائي!")
print("="*60)
