#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
جلسة تحسين pH مكثفة - Soil pH Intensive Adjustment
"""
import sys
import time
sys.path.insert(0, 'src')

from modules.auto_adjuster import SoilAutoAdjuster
from modules.soil_monitor import SoilMonitor

print('🔧 بدء جلسة تحسين pH مكثفة...')
print('='*50)

# إنشاء المراقب والمعدل
monitor = SoilMonitor()
adjuster = SoilAutoAdjuster()

print('📊 المشكلة الحالية:')
print('   - متوسط pH: 7.22 (مرتفع)')
print('   - الهدف: 6.8 ± 0.2')
print('   - الفرق: +0.42 (يتطلب تصحيح)')
print('')

# 3 دورات تصحيح مكثفة
for i in range(1, 4):
    print(f'🌀 دورة التصحيح #{i}')
    print('-'*30)
    
    # محاكاة بيانات pH مرتفعة تدريجياً
    soil_data = {
        'ph': 7.22 - (i * 0.1),
        'moisture': 65,
        'temperature': 25,
        'timestamp': '2026-01-12T15:15:00'
    }
    
    print(f'📡 قراءة التربة:')
    print(f'   - pH: {soil_data["ph"]}')
    print(f'   - الرطوبة: {soil_data["moisture"]}%')
    print(f'   - الحرارة: {soil_data["temperature"]}°C')
    
    # تشغيل التعديل التلقائي
    adjuster.run_auto_adjustment_cycle(soil_data)
    
    if i < 3:
        print('⏳ انتظار 2 ثواني...')
        time.sleep(2)
        print('')

print('='*50)
print('✅ اكتملت جلسة تحسين pH!')
print('📊 النتائج المتوقعة:')
print('   - pH الجديد: ~6.92 (مقبول)')
print('   - عدد الإجراءات: 3-6 إجراء')
print('   - الوقت المستغرق: ~10 ثواني')
print('')
print('📍 يمكنك التحقق من:')
print('   - logs/auto_adjust.log (سجل الإجراءات)')
print('   - data/processed/actions_taken.json (تفاصيل)')
