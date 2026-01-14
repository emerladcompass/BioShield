#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولد التقارير - مع دفع التقارير الأسبوعية والشهرية
"""

import os
from datetime import datetime, timedelta
from pathlib import Path

class ReportGenerator:
    def __init__(self):
        # استخدام المسار الصحيح
        self.base_dir = Path(__file__).parent.parent.parent
        
        # إنشاء جميع المجلدات المطلوبة
        self.daily_dir = self.base_dir / "reports" / "daily"
        self.weekly_dir = self.base_dir / "reports" / "weekly"
        self.monthly_dir = self.base_dir / "reports" / "monthly"
        
        # إنشاء المجلدات إذا لم تكن موجودة
        self.daily_dir.mkdir(parents=True, exist_ok=True)
        self.weekly_dir.mkdir(parents=True, exist_ok=True)
        self.monthly_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_custom_recommendations(self, all_data):
        """توليد توصيات مخصصة بناء على البيانات الفعلية"""
        if not all_data:
            return ["لا توجد بيانات كافية للتوصيات"]
        
        recommendations = []
        
        # حساب المتوسطات
        avg_ph = sum(d['ph'] for d in all_data) / len(all_data)
        avg_moisture = sum(d['moisture'] for d in all_data) / len(all_data)
        avg_temp = sum(d['temperature'] for d in all_data) / len(all_data)
        
        # تحليل pH
        if 6.0 <= avg_ph <= 7.0:
            recommendations.append(f"مستوى pH مثالي ({avg_ph:.2f})")
        elif avg_ph < 6.0:
            recommendations.append(f"إضافة مواد قلوية لرفع pH (المتوسط: {avg_ph:.2f})")
        else:
            recommendations.append(f"إضافة مواد حمضية لخفض pH (المتوسط: {avg_ph:.2f})")
        
        # تحليل الرطوبة
        if 50 <= avg_moisture <= 65:
            recommendations.append(f"مستوى رطوبة مثالي ({avg_moisture:.0f}%)")
        elif avg_moisture < 50:
            recommendations.append(f"زيادة الري - الرطوبة منخفضة ({avg_moisture:.0f}%)")
        else:
            recommendations.append(f"تقليل الري - الرطوبة مرتفعة ({avg_moisture:.0f}%)")
        
        # تحليل الحرارة
        if 20 <= avg_temp <= 25:
            recommendations.append(f"درجة حرارة مثالية ({avg_temp:.0f}°C)")
        elif avg_temp < 20:
            recommendations.append(f"الحرارة منخفضة ({avg_temp:.0f}°C)")
        else:
            recommendations.append(f"الحرارة مرتفعة ({avg_temp:.0f}°C)")
        
        # تحليل التنبيهات
        statuses = [d.get('status', '') for d in all_data]
        critical_count = statuses.count('CRITICAL')
        warning_count = statuses.count('NEEDS_ATTENTION')
        
        if critical_count > 0:
            recommendations.append(f"⚠️ فحص عاجل - {critical_count} قراءة حرجة")
        if warning_count > 1:
            recommendations.append(f"🔶 انتباه - {warning_count} قراءة تحتاج مراقبة")
        
        return recommendations
    
    def generate_daily_report(self, all_data):
        """إنشاء تقرير يومي من بيانات كل الدورة"""
        if not all_data:
            return {"error": "لا توجد بيانات"}
        
        total_samples = len(all_data)
        
        # حساب الإحصائيات
        statuses = [d.get('status', '') for d in all_data]
        critical_alerts = statuses.count('CRITICAL')
        warning_alerts = statuses.count('NEEDS_ATTENTION')
        total_alerts = critical_alerts + warning_alerts
        
        # تحليل دقيق للبيانات
        key_findings = []
        avg_ph = sum(d['ph'] for d in all_data) / total_samples
        avg_moisture = sum(d['moisture'] for d in all_data) / total_samples
        avg_temp = sum(d['temperature'] for d in all_data) / total_samples
        
        # تحليل pH
        if 6.0 <= avg_ph <= 7.0:
            key_findings.append(f"مستوى pH متوازن ({avg_ph:.2f})")
        elif avg_ph < 6.0:
            key_findings.append(f"الحموضة مرتفعة ({avg_ph:.2f}) - يحتاج تعديل")
        else:
            key_findings.append(f"القلوية مرتفعة ({avg_ph:.2f}) - يحتاج تعديل")
        
        # تحليل الرطوبة
        if 50 <= avg_moisture <= 65:
            key_findings.append(f"الرطوبة متوازنة ({avg_moisture:.0f}%)")
        elif avg_moisture < 50:
            key_findings.append(f"الرطوبة منخفضة ({avg_moisture:.0f}%) - يحتاج ري")
        else:
            key_findings.append(f"الرطوبة مرتفعة ({avg_moisture:.0f}%) - تقليل الري")
        
        # تحليل الحرارة
        if 20 <= avg_temp <= 25:
            key_findings.append(f"درجة حرارة مثالية ({avg_temp:.0f}°C)")
        elif avg_temp < 20:
            key_findings.append(f"الحرارة منخفضة ({avg_temp:.0f}°C)")
        else:
            key_findings.append(f"الحرارة مرتفعة ({avg_temp:.0f}°C)")
        
        # تحديد الحالة العامة
        if critical_alerts > 0:
            soil_health = "POOR"
            overall_status = "CRITICAL"
        elif warning_alerts > total_samples * 0.3:
            soil_health = "FAIR"
            overall_status = "NEEDS_ATTENTION"
        elif warning_alerts > 0:
            soil_health = "GOOD"
            overall_status = "MONITOR"
        else:
            soil_health = "EXCELLENT"
            overall_status = "OPTIMAL"
        
        report = {
            "metadata": {
                "report_id": f"DAILY-{datetime.now().date()}",
                "generated_at": datetime.now().isoformat(),
                "system_version": "B_Agro_Immunity v3.0",
                "report_type": "daily"
            },
            "summary": {
                "total_samples": total_samples,
                "total_alerts": total_alerts,
                "critical_alerts": critical_alerts,
                "warning_alerts": warning_alerts,
                "soil_health": soil_health,
                "overall_status": overall_status,
                "average_ph": round(avg_ph, 2),
                "average_moisture": round(avg_moisture, 1),
                "average_temperature": round(avg_temp, 1),
                "key_findings": key_findings
            },
            "recommendations": self.generate_custom_recommendations(all_data),
            "all_data": all_data
        }
        return report
    
    def save_report(self, report, file_path=None):
        """حفظ التقرير اليومي"""
        if file_path is None:
            # إنشاء اسم ملف يومي
            today = datetime.now().strftime("%Y-%m-%d")
            file_path = self.daily_dir / f"report_{today}.txt"
        
        # التأكد من أن file_path هو Path object
        if not isinstance(file_path, Path):
            file_path = Path(file_path)
        
        # التأكد من وجود المجلد
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("📅 تقرير يومي - BioShield\n")
            f.write("="*60 + "\n")
            f.write(f"📋 رقم التقرير: {report['metadata']['report_id']}\n")
            f.write(f"⏰ وقت التوليد: {report['metadata']['generated_at']}\n")
            f.write(f"🔧 إصدار النظام: {report['metadata']['system_version']}\n")
            f.write("="*60 + "\n\n")
            
            f.write("📊 بيانات كل دورة:\n")
            for idx, d in enumerate(report['all_data'], 1):
                f.write(f"🌀 دورة رقم {idx}\n")
                f.write(f"   - pH: {d.get('ph', 'N/A')}\n")
                f.write(f"   - الرطوبة: {d.get('moisture', 'N/A')}%\n")
                f.write(f"   - الحرارة: {d.get('temperature', 'N/A')}°C\n")
                f.write(f"   - الحالة: {d.get('status', 'UNKNOWN')}\n")
                f.write("   " + "-"*40 + "\n")
            
            f.write("\n📋 ملخص اليوم:\n")
            summary = report['summary']
            f.write(f"🔢 عدد العينات: {summary['total_samples']}\n")
            f.write(f"⚠️ عدد التنبيهات: {summary['total_alerts']}\n")
            f.write(f"🔴 تنبيهات حرجة: {summary['critical_alerts']}\n")
            f.write(f"🟡 تنبيهات تحذير: {summary['warning_alerts']}\n")
            f.write(f"🌱 صحة التربة: {summary['soil_health']}\n")
            f.write(f"📊 الحالة العامة: {summary['overall_status']}\n")
            f.write(f"📈 متوسط pH: {summary['average_ph']}\n")
            f.write(f"💧 متوسط الرطوبة: {summary['average_moisture']}%\n")
            f.write(f"🌡️ متوسط الحرارة: {summary['average_temperature']}°C\n")
            
            if summary['key_findings']:
                f.write("\n🔍 النتائج الرئيسية:\n")
                for k in summary['key_findings']:
                    f.write(f" • {k}\n")
            
            if report['recommendations']:
                f.write("\n💡 التوصيات:\n")
                for r in report['recommendations']:
                    f.write(f" • {r}\n")
            
            f.write("\n" + "="*60 + "\n")
            f.write("📁 الملفات: daily/weekly/monthly\n")
            f.write("="*60 + "\n")
        
        print(f"✅ تم حفظ التقرير اليومي في: {file_path}")
        
        # دفع نسخة للأسبوعي إذا كان اليوم أحد (بداية الأسبوع)
        if datetime.now().weekday() == 6:  # 6 = الأحد
            self._push_to_weekly(report)
        
        # دفع نسخة للشهري إذا كان اليوم الأول من الشهر
        if datetime.now().day == 1:
            self._push_to_monthly(report)
        
        return str(file_path)
    
    def _push_to_weekly(self, daily_report):
        """دفع تقرير للأسبوعي"""
        try:
            # تاريخ بداية الأسبوع (الأحد)
            week_start = datetime.now() - timedelta(days=datetime.now().weekday())
            week_str = week_start.strftime("%Y-%m-%d")
            
            weekly_file = self.weekly_dir / f"weekly_report_{week_str}.txt"
            
            with open(weekly_file, 'w', encoding='utf-8') as f:
                f.write("📅 تقرير أسبوعي - BioShield\n")
                f.write("="*60 + "\n")
                f.write(f"📅 الأسبوع: {week_str}\n")
                f.write(f"⏰ وقت التوليد: {datetime.now().isoformat()}\n")
                f.write("="*60 + "\n\n")
                
                f.write("📊 ملخص من التقرير اليومي:\n")
                f.write("-"*40 + "\n")
                
                summary = daily_report['summary']
                f.write(f"🌱 صحة التربة: {summary['soil_health']}\n")
                f.write(f"📊 الحالة العامة: {summary['overall_status']}\n")
                f.write(f"📈 متوسط pH: {summary['average_ph']}\n")
                f.write(f"💧 متوسط الرطوبة: {summary['average_moisture']}%\n")
                f.write(f"🌡️ متوسط الحرارة: {summary['average_temperature']}°C\n")
                
                if daily_report['recommendations']:
                    f.write("\n💡 توصيات الأسبوع:\n")
                    for r in daily_report['recommendations']:
                        f.write(f" • {r}\n")
                
                f.write("\n" + "="*60 + "\n")
            
            print(f"📁 تم دفع نسخة أسبوعية إلى: {weekly_file}")
            
        except Exception as e:
            print(f"⚠️ خطأ في حفظ الأسبوعي: {e}")
    
    def _push_to_monthly(self, daily_report):
        """دفع تقرير للشهري"""
        try:
            current_month = datetime.now().strftime("%Y-%m")
            monthly_file = self.monthly_dir / f"monthly_report_{current_month}.txt"
            
            with open(monthly_file, 'w', encoding='utf-8') as f:
                f.write("📅 تقرير شهري - BioShield\n")
                f.write("="*60 + "\n")
                f.write(f"📅 الشهر: {current_month}\n")
                f.write(f"⏰ وقت التوليد: {datetime.now().isoformat()}\n")
                f.write("="*60 + "\n\n")
                
                f.write("📊 ملخص من التقرير اليومي:\n")
                f.write("-"*40 + "\n")
                
                summary = daily_report['summary']
                f.write(f"🌱 صحة التربة هذا الشهر: {summary['soil_health']}\n")
                f.write(f"📊 الحالة العامة: {summary['overall_status']}\n")
                f.write(f"📈 متوسط pH: {summary['average_ph']}\n")
                f.write(f"💧 متوسط الرطوبة: {summary['average_moisture']}%\n")
                f.write(f"🌡️ متوسط الحرارة: {summary['average_temperature']}°C\n")
                
                f.write("\n📋 ملاحظات شهرية:\n")
                f.write("• مراجعة أداء التربة على مدار الشهر\n")
                f.write("• التخطيط للزراعة الشهر القادم\n")
                f.write("• صيانة الأجهزة والمعدات\n")
                
                f.write("\n" + "="*60 + "\n")
            
            print(f"📁 تم دفع نسخة شهرية إلى: {monthly_file}")
            
        except Exception as e:
            print(f"⚠️ خطأ في حفظ الشهري: {e}")

# اختبار مباشر
if __name__ == "__main__":
    print("🧪 اختبار ReportGenerator مع weekly/monthly")
    print("="*50)
    
    rg = ReportGenerator()
    
    # بيانات اختبارية
    test_data = [
        {"ph": 6.5, "moisture": 55, "temperature": 22, "status": "GOOD"},
        {"ph": 6.3, "moisture": 50, "temperature": 24, "status": "GOOD"},
        {"ph": 6.7, "moisture": 60, "temperature": 20, "status": "EXCELLENT"}
    ]
    
    report = rg.generate_daily_report(test_data)
    saved_path = rg.save_report(report)
    
    print(f"\n📊 تم إنشاء التقرير بنجاح")
    print(f"📁 الحفظ في: {saved_path}")
    
    # عرض هيكل المجلدات
    print(f"\n📁 هيكل مجلدات التقارير:")
    print(f"   daily: {rg.daily_dir}")
    print(f"   weekly: {rg.weekly_dir}")
    print(f"   monthly: {rg.monthly_dir}")
