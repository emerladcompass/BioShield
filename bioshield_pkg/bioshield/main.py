#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
النظام الرئيسي: قراءة التربة + تعديل تلقائي + تقرير يومي
"""

import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, 'src')

from modules.soil_monitor import SoilMonitor
from modules.auto_adjuster import SoilAutoAdjuster
from modules.report_generator import ReportGenerator

def main():
    monitor = SoilMonitor()
    adjuster = SoilAutoAdjuster()  # تهيئة بدون أي معاملات
    report_gen = ReportGenerator()

    daily_data = []
    total_cycles = 5

    for i in range(1, total_cycles + 1):
        print(f"\n🌀 الدورة رقم {i}")
        soil_data = monitor.simulate_sensor_reading()

        # تنفيذ تعديل تلقائي كامل (دالة موجودة في الكلاس)
        analysis = adjuster.run_auto_adjustment_cycle(soil_data)

        # تخزين بيانات الدورة
        daily_data.append({
            "ph": soil_data.get("ph", 0),
            "moisture": soil_data.get("moisture", 0),
            "temperature": soil_data.get("temperature", 0),
            "status": analysis.get("status", "UNKNOWN")
        })

        time.sleep(1)

    # توليد التقرير اليومي
    report = report_gen.generate_daily_report(daily_data)
    report_file = Path("reports/daily") / f"report_{datetime.now().date()}.txt"
    report_gen.save_report(report, report_file)

    print(f"\n✅ تم حفظ التقرير اليومي: {report_file}")
    print("🎉 جميع الأنظمة اكتملت بنجاح!")

if __name__ == "__main__":
    main()
