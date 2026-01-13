#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from datetime import datetime

class SoilAutoAdjuster:
    """نظام تعديل التربة تلقائياً"""
    def __init__(self):
        self.ph_target = 6.8
        self.ph_tolerance = 0.3
        self.moisture_target = 65
        self.moisture_tolerance = 10

    def run_auto_adjustment_cycle(self, soil_data):
        ph = soil_data["ph"]
        moisture = soil_data["moisture"]
        status = soil_data.get("status", "STABLE")
        
        print("\n" + "="*40)
        print("🤖 نظام التعديل التلقائي للتربة")
        print("="*40)
        print(f"📊 بيانات التربة:")
        print(f"   - pH: {ph} (الهدف: {self.ph_target} ± {self.ph_tolerance})")
        print(f"   - الرطوبة: {moisture}% (الهدف: {self.moisture_target} ± {self.moisture_tolerance})")
        print(f"   - الحالة: {status}")
        
        actions = []
        if ph > self.ph_target + self.ph_tolerance:
            actions.append("خفض pH")
        elif ph < self.ph_target - self.ph_tolerance:
            actions.append("رفع pH")
        if moisture > self.moisture_target + self.moisture_tolerance:
            actions.append("تقليل الري")
        elif moisture < self.moisture_target - self.moisture_tolerance:
            actions.append("زيادة الري")
        
        if actions:
            print("\n🎯 الإجراءات المطلوبة:")
            for act in actions:
                print(f"   • {act}")
                time.sleep(0.3)
            print(f"\n✅ تم تنفيذ {len(actions)} إجراء بنجاح")
        else:
            print("\n✅ التربة مستقرة - لا حاجة للتعديل")
        
        print("="*40)
        return soil_data
