#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

class ReportFormatter:
    """حفظ التقرير اليومي بشكل مرتب"""
    def save_daily_report(self, report, report_date):
        path = os.path.join("reports", "daily")
        os.makedirs(path, exist_ok=True)
        filename = os.path.join(path, f"report_{report_date}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Daily Report Summary\n")
            f.write("="*60 + "\n")
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"✅ Report saved in {filename}")
