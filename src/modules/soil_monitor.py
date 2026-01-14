#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مراقب التربة - نسخة محسنة مع تحليل واقعي
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
        ph = round(random.uniform(5.5, 7.5), 1)
        moisture = random.randint(40, 70)
        temperature = random.randint(18, 30)
        
        return {
            "ph": ph,
            "moisture": moisture,
            "temperature": temperature,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_reading_with_analysis(self):
        """الحصول على قراءة مع تحليل متقدم"""
        data = self.simulate_sensor_reading()
        self.last_reading = data
        
        ph = data["ph"]
        moisture = data["moisture"]
        temperature = data["temperature"]
        
        # تحليل pH متقدم
        if 6.0 <= ph <= 7.0:
            ph_category = "OPTIMAL"
            ph_status = "مثالي"
            ph_score = 100
        elif 5.5 <= ph < 6.0:
            ph_category = "SLIGHTLY_ACIDIC"
            ph_status = "حمضي قليلاً"
            ph_score = 70
        elif ph < 5.5:
            ph_category = "ACIDIC"
            ph_status = "حمضي"
            ph_score = 40
        elif 7.0 < ph <= 7.5:
            ph_category = "SLIGHTLY_ALKALINE"
            ph_status = "قلوي قليلاً"
            ph_score = 70
        else:
            ph_category = "ALKALINE"
            ph_status = "قلوي"
            ph_score = 40
        
        # تحليل الرطوبة متقدم
        if 50 <= moisture <= 65:
            moisture_category = "OPTIMAL"
            moisture_status = "مثالي"
            moisture_score = 100
        elif 40 <= moisture < 50:
            moisture_category = "SLIGHTLY_DRY"
            moisture_status = "جاف قليلاً"
            moisture_score = 70
        elif moisture < 40:
            moisture_category = "DRY"
            moisture_status = "جاف"
            moisture_score = 40
        elif 65 < moisture <= 70:
            moisture_category = "SLIGHTLY_WET"
            moisture_status = "رطب قليلاً"
            moisture_score = 70
        else:
            moisture_category = "WET"
            moisture_status = "رطب"
            moisture_score = 40
        
        # تحليل الحرارة متقدم
        if 20 <= temperature <= 25:
            temp_category = "OPTIMAL"
            temp_status = "مثالي"
            temp_score = 100
        elif 18 <= temperature < 20:
            temp_category = "SLIGHTLY_COLD"
            temp_status = "بارد قليلاً"
            temp_score = 70
        elif temperature < 18:
            temp_category = "COLD"
            temp_status = "بارد"
            temp_score = 40
        elif 25 < temperature <= 28:
            temp_category = "SLIGHTLY_HOT"
            temp_status = "حار قليلاً"
            temp_score = 70
        else:
            temp_category = "HOT"
            temp_status = "حار"
            temp_score = 40
        
        # الحالة العامة - حساب متقدم
        avg_score = (ph_score + moisture_score + temp_score) / 3
        
        if avg_score >= 85:
            status = "EXCELLENT"
            status_ar = "ممتاز"
        elif avg_score >= 70:
            status = "GOOD"
            status_ar = "جيد"
        elif avg_score >= 55:
            status = "FAIR"
            status_ar = "مقبول"
        elif avg_score >= 40:
            status = "NEEDS_ATTENTION"
            status_ar = "يحتاج انتباه"
        else:
            status = "CRITICAL"
            status_ar = "حرج"
        
        return {
            **data,
            "ph_category": ph_category,
            "ph_status": ph_status,
            "ph_score": ph_score,
            "moisture_category": moisture_category,
            "moisture_status": moisture_status,
            "moisture_score": moisture_score,
            "temperature_category": temp_category,
            "temperature_status": temp_status,
            "temperature_score": temp_score,
            "status": status,
            "status_ar": status_ar,
            "overall_score": avg_score
        }
    
    def get_status_summary(self):
        """ملخص حالة التربة"""
        if not self.last_reading:
            return "لا توجد قراءات حديثة"
        
        reading = self.get_reading_with_analysis()
        
        return f"""
📊 ملخص حالة التربة:
   درجة الحموضة: {reading['ph']} ({reading['ph_status']}) - {reading['ph_score']}%
   الرطوبة: {reading['moisture']}% ({reading['moisture_status']}) - {reading['moisture_score']}%
   الحرارة: {reading['temperature']}°C ({reading['temperature_status']}) - {reading['temperature_score']}%
   الحالة العامة: {reading['status_ar']} ({reading['overall_score']:.0f}%)
"""

# اختبار مباشر
if __name__ == "__main__":
    print("🧪 اختبار SoilMonitor المحسن")
    print("="*50)
    
    monitor = SoilMonitor()
    
    # اختبار 3 قراءات
    for i in range(3):
        reading = monitor.get_reading_with_analysis()
        print(f"📈 القراءة {i+1}:")
        print(f"   pH: {reading['ph']} ({reading['ph_status']})")
        print(f"   الرطوبة: {reading['moisture']}% ({reading['moisture_status']})")
        print(f"   الحرارة: {reading['temperature']}°C ({reading['temperature_status']})")
        print(f"   الحالة: {reading['status_ar']} ({reading['overall_score']:.0f}%)")
        print()
    
    # عرض الملخص
    print(monitor.get_status_summary())
