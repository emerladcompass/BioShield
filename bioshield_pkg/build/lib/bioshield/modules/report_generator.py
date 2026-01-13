#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Report Generator - حفظ تقارير التربة اليومية بصيغة TXT منسقة
"""
import os
from datetime import datetime
from pathlib import Path

class ReportGenerator:
    def __init__(self):
        self.daily_dir = Path("reports/daily")
        self.daily_dir.mkdir(parents=True, exist_ok=True)

    def generate_daily_report(self, all_data):
        """إنشاء تقرير يومي من بيانات كل الدورة"""
        total_samples = len(all_data)
        total_alerts = sum(1 for d in all_data if d['status'] != 'STABLE')
        critical_alerts = sum(1 for d in all_data if d['status'] == 'CRITICAL')
        key_findings = []
        if any(d['ph'] > 7.0 for d in all_data):
            key_findings.append("متوسط pH خارج النطاق الأمثل")
        if any(d['moisture'] > 80 for d in all_data):
            key_findings.append("تنبيهات الرطوبة متكررة")

        report = {
            "metadata": {
                "report_id": f"DAILY-{datetime.now().date()}",
                "generated_at": datetime.now().isoformat(),
                "system_version": "B_Agro_Immunity v3.0"
            },
            "summary": {
                "total_samples": total_samples,
                "total_alerts": total_alerts,
                "critical_alerts": critical_alerts,
                "soil_health": "FAIR" if total_alerts else "EXCELLENT",
                "overall_status": "NEEDS_ATTENTION" if total_alerts else "OPTIMAL",
                "key_findings": key_findings
            },
            "recommendations": [
                "زيادة الري حسب الرطوبة",
                "معايرة مستشعرات pH",
                "مراجعة مستويات المواد الغذائية للتربة"
            ],
            "next_steps": [
                "جمع بيانات إضافية الأسبوع القادم",
                "صيانة الأجهزة",
                "مراقبة الاتجاهات"
            ],
            "all_data": all_data
        }
        return report

    def save_report(self, report, file_path):
        """حفظ التقرير بصيغة TXT منسقة"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("Daily Report Summary\n")
            f.write("="*60 + "\n")
            f.write(f"Report ID: {report['metadata']['report_id']}\n")
            f.write(f"Generated At: {report['metadata']['generated_at']}\n")
            f.write(f"System Version: {report['metadata']['system_version']}\n")
            f.write("="*60 + "\n\n")

            f.write("📊 Data Per Cycle:\n")
            for idx, d in enumerate(report['all_data'], 1):
                f.write(f"🌀 دورة رقم {idx}\n")
                f.write(f"   - pH: {d['ph']}\n")
                f.write(f"   - الرطوبة: {d['moisture']}%\n")
                f.write(f"   - الحرارة: {d['temperature']}°C\n")
                f.write(f"   - الحالة: {d['status']}\n")
                f.write("-"*40 + "\n")

            f.write("\n📋 Daily Summary:\n")
            summary = report['summary']
            f.write(f"Total Samples: {summary['total_samples']}\n")
            f.write(f"Total Alerts: {summary['total_alerts']}\n")
            f.write(f"Critical Alerts: {summary['critical_alerts']}\n")
            f.write(f"Soil Health: {summary['soil_health']}\n")
            f.write(f"Overall Status: {summary['overall_status']}\n")
            if summary['key_findings']:
                f.write("Key Findings:\n")
                for k in summary['key_findings']:
                    f.write(f" - {k}\n")

            f.write("\nRecommendations:\n")
            for r in report['recommendations']:
                f.write(f" - {r}\n")

            f.write("\nNext Steps:\n")
            for n in report['next_steps']:
                f.write(f" - {n}\n")

            f.write("\n" + "="*60 + "\n")
        print(f"✅ Report saved in {file_path}")
