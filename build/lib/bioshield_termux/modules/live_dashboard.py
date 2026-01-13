#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
لوحة التحكم الحيوية - Live Dashboard
"""
import os
import json
import time
from datetime import datetime
from pathlib import Path

class LiveDashboard:
    def __init__(self):
        self.dashboard_file = "data/processed/dashboard.json"
        self.stats_file = "data/processed/system_stats.json"
        self.setup_directories()
        
        # إحصائيات النظام
        self.stats = {
            "start_time": datetime.now().isoformat(),
            "total_cycles": 0,
            "alerts_count": 0,
            "critical_alerts": 0,
            "soil_samples": 0,
            "water_tests": 0
        }
    
    def setup_directories(self):
        """إعداد المجلدات"""
        Path("data/processed").mkdir(parents=True, exist_ok=True)
    
    def update_dashboard(self, module, data):
        """تحديث لوحة التحكم"""
        try:
            # تحميل البيانات الحالية
            if os.path.exists(self.dashboard_file):
                with open(self.dashboard_file, 'r') as f:
                    dashboard = json.load(f)
            else:
                dashboard = {
                    "last_updated": "",
                    "modules": {},
                    "system_status": "OPERATIONAL",
                    "alerts": [],
                    "performance": {}
                }
            
            # تحديث البيانات
            dashboard["last_updated"] = datetime.now().isoformat()
            dashboard["modules"][module] = {
                "data": data,
                "timestamp": datetime.now().isoformat()
            }
            
            # تحديث الإحصائيات
            self.stats["total_cycles"] += 1
            if "alerts" in data and data["alerts"]:
                self.stats["alerts_count"] += len(data["alerts"])
                if any("🚨" in str(alert) for alert in data["alerts"]):
                    self.stats["critical_alerts"] += 1
            
            # حفظ لوحة التحكم
            with open(self.dashboard_file, 'w') as f:
                json.dump(dashboard, f, indent=2, ensure_ascii=False)
            
            # حفظ الإحصائيات
            with open(self.stats_file, 'w') as f:
                json.dump(self.stats, f, indent=2, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            print(f"[!] خطأ في تحديث لوحة التحكم: {e}")
            return False
    
    def display_dashboard(self):
        """عرض لوحة التحكم"""
        if not os.path.exists(self.dashboard_file):
            print("[!] لا توجد بيانات للعرض")
            return
        
        try:
            with open(self.dashboard_file, 'r') as f:
                dashboard = json.load(f)
            
            print("\n" + "="*60)
            print("📊 لوحة تحكم B_Agro_Immunity الحيوية")
            print("="*60)
            print(f"🕒 آخر تحديث: {dashboard.get('last_updated', 'N/A')}")
            print(f"📈 حالة النظام: {dashboard.get('system_status', 'UNKNOWN')}")
            print("-"*60)
            
            # عرض بيانات الوحدات
            modules = dashboard.get("modules", {})
            if modules:
                for module_name, module_data in modules.items():
                    print(f"\n🔧 {module_name.upper()}:")
                    data = module_data.get("data", {})
                    
                    if "status" in data:
                        status_icon = "✅" if data["status"] == "OPTIMAL" else "⚠️" if data["status"] == "WARNING" else "🚨"
                        print(f"   {status_icon} الحالة: {data['status']}")
                    
                    if "alerts" in data and data["alerts"]:
                        print(f"   ⚠️  التنبيهات: {len(data['alerts'])}")
                        for alert in data["alerts"][:3]:  # عرض أول 3 تنبيهات فقط
                            print(f"     • {alert}")
            
            # عرض الإحصائيات
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r') as f:
                    stats = json.load(f)
                
                print("\n" + "-"*60)
                print("📈 إحصائيات النظام:")
                print(f"   • دورات المراقبة: {stats.get('total_cycles', 0)}")
                print(f"   • إجمالي التنبيهات: {stats.get('alerts_count', 0)}")
                print(f"   • تنبيهات حرجة: {stats.get('critical_alerts', 0)}")
                print(f"   • عينات التربة: {stats.get('soil_samples', 0)}")
                print(f"   • اختبارات المياه: {stats.get('water_tests', 0)}")
            
            print("="*60)
            
        except Exception as e:
            print(f"[!] خطأ في عرض لوحة التحكم: {e}")
    
    def run_live_monitoring(self, interval=5, duration=30):
        """تشغيل مراقبة حية"""
        print(f"\n🔄 بدء المراقبة الحية (فاصل: {interval}ث، مدة: {duration}ث)")
        print("="*60)
        
        from modules.soil_monitor import SoilMonitor
        
        soil_monitor = SoilMonitor()
        start_time = time.time()
        cycle = 1
        
        try:
            while time.time() - start_time < duration:
                print(f"\n🌀 الدورة رقم {cycle}")
                print("-"*40)
                
                # محاكاة قراءة المستشعار
                sensor_data = soil_monitor.simulate_sensor_reading()
                analysis = soil_monitor.analyze_soil_health(sensor_data)
                
                # تحديث لوحة التحكم
                self.update_dashboard("soil_monitor", analysis)
                
                # عرض البيانات الحية
                print(f"🌱 قراءات التربة:")
                print(f"   - pH: {sensor_data['ph']}")
                print(f"   - الرطوبة: {sensor_data['moisture']}%")
                print(f"   - الحرارة: {sensor_data['temperature']}°C")
                print(f"   - الحالة: {analysis['status']}")
                
                if analysis['alerts']:
                    print(f"   ⚠️  تنبيهات: {', '.join(analysis['alerts'][:2])}")
                
                # عرض لوحة التحكم كل 3 دورات
                if cycle % 3 == 0:
                    self.display_dashboard()
                
                cycle += 1
                time.sleep(interval)
            
            print("\n" + "="*60)
            print("✅ اكتملت المراقبة الحية!")
            self.display_dashboard()
            
        except KeyboardInterrupt:
            print("\n\n🛑 تم إيقاف المراقبة الحية بواسطة المستخدم")
            self.display_dashboard()

if __name__ == "__main__":
    dashboard = LiveDashboard()
    dashboard.run_live_monitoring(interval=3, duration=20)
