#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مراقب التربة - نسخة مبسطة مع محاكاة
"""

import random
from datetime import datetime

class SoilMonitor:
    def __init__(self):
        self.sensor_active = True
        self.last_reading = None
    
    def simulate_sensor_reading(self):
        """محاكاة قراءة أجهزة الاستشعار"""
        # قيم واقعية لتربة زراعية
        ph = round(random.uniform(5.5, 7.5), 1)  # pH بين 5.5 و 7.5
        moisture = random.randint(40, 70)  # رطوبة بين 40% و 70%
        temperature = random.randint(18, 30)  # حرارة بين 18 و 30
        
        return {
            "ph": ph,
            "moisture": moisture,
            "temperature": temperature,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_reading_with_analysis(self):
        """الحصول على قراءة مع التحليل"""
        data = self.simulate_sensor_reading()
        self.last_reading = data
        
        # تحليل pH
        ph = data["ph"]
        if 6.0 <= ph <= 7.0:
            ph_category = "OPTIMAL"
            ph_status = "مثالي"
        elif ph < 6.0:
            ph_category = "ACIDIC"
            ph_status = "حمضي"
        else:
            ph_category = "ALKALINE"
            ph_status = "قلوي"
        
        # تحليل الرطوبة
        moisture = data["moisture"]
        if 50 <= moisture <= 65:
            moisture_category = "OPTIMAL"
            moisture_status = "مثالي"
        elif moisture < 50:
            moisture_category = "DRY"
            moisture_status = "جاف"
        else:
            moisture_category = "WET"
            moisture_status = "رطب"
        
        # تحليل الحرارة
        temp = data["temperature"]
        if 20 <= temp <= 25:
            temp_category = "OPTIMAL"
            temp_status = "مثالي"
        elif temp < 20:
            temp_category = "COLD"
            temp_status = "بارد"
        else:
            temp_category = "HOT"
            temp_status = "حار"
        
        # الحالة العامة
        if ph_category == "OPTIMAL" and moisture_category == "OPTIMAL":
            status = "EXCELLENT"
        else:
            status = "STABLE"
        
        return {
            **data,
            "ph_category": ph_category,
            "ph_status": ph_status,
            "moisture_category": moisture_category,
            "moisture_status": moisture_status,
            "temperature_category": temp_category,
            "temperature_status": temp_status,
            "status": status,
            "status_ar": "مستقر" if status == "STABLE" else "ممتاز"
        }
    
    def get_status_summary(self):
        """ملخص حالة التربة"""
        if not self.last_reading:
            return "لا توجد قراءات حديثة"
        
        reading = self.get_reading_with_analysis()
        
        return f"""
📊 ملخص حالة التربة:
   درجة الحموضة: {reading['ph']} ({reading['ph_status']})
   الرطوبة: {reading['moisture']}% ({reading['moisture_status']})
   الحرارة: {reading['temperature']}°C ({reading['temperature_status']})
   الحالة العامة: {reading['status_ar']}
"""

# اختبار مباشر
if __name__ == "__main__":
    print("🧪 اختبار SoilMonitor")
    print("="*50)
    
    monitor = SoilMonitor()
    
    # اختبار 3 قراءات
    for i in range(3):
        reading = monitor.get_reading_with_analysis()
        print(f"📈 القراءة {i+1}:")
        print(f"   pH: {reading['ph']} ({reading['ph_status']})")
        print(f"   الرطوبة: {reading['moisture']}% ({reading['moisture_status']})")
        print(f"   الحرارة: {reading['temperature']}°C ({reading['temperature_status']})")
        print()
    
    # عرض الملخص
    print(monitor.get_status_summary())
