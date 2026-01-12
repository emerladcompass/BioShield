#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام التنبؤ الذكي - AI Prediction System
"""
import json
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

class AIPredictor:
    def __init__(self):
        self.model_file = "data/models/ai_model.json"
        self.predictions_file = "data/processed/predictions.json"
        self.history_days = 7
        
    def train_model(self, historical_data):
        """تدريب نموذج تنبؤ مبسط"""
        model = {
            "trained_at": datetime.now().isoformat(),
            "ph_trend": self.calculate_trend(historical_data, "ph"),
            "moisture_trend": self.calculate_trend(historical_data, "moisture"),
            "temperature_trend": self.calculate_trend(historical_data, "temperature"),
            "anomaly_patterns": self.detect_anomalies(historical_data)
        }
        
        # حفظ النموذج
        Path("data/models").mkdir(parents=True, exist_ok=True)
        with open(self.model_file, 'w') as f:
            json.dump(model, f, indent=2)
        
        return model
    
    def calculate_trend(self, data, key):
        """حساب اتجاه البيانات"""
        values = [d.get(key, 0) for d in data if key in d]
        if len(values) < 2:
            return "STABLE"
        
        # حساب الميل
        x = np.arange(len(values))
        y = np.array(values)
        z = np.polyfit(x, y, 1)
        slope = z[0]
        
        if slope > 0.1:
            return "INCREASING"
        elif slope < -0.1:
            return "DECREASING"
        else:
            return "STABLE"
    
    def detect_anomalies(self, data):
        """كشف الحالات الشاذة"""
        anomalies = []
        
        # تحليل pH
        ph_values = [d.get("ph", 7) for d in data if "ph" in d]
        if ph_values:
            ph_mean = np.mean(ph_values)
            ph_std = np.std(ph_values)
            
            for i, ph in enumerate(ph_values):
                if abs(ph - ph_mean) > 2 * ph_std:
                    anomalies.append({
                        "type": "pH_ANOMALY",
                        "value": ph,
                        "expected": round(ph_mean, 2),
                        "timestamp": data[i].get("timestamp", "")
                    })
        
        return anomalies
    
    def predict_next_24h(self, current_data, historical_data):
        """التنبؤ بالـ 24 ساعة القادمة"""
        predictions = {
            "generated_at": datetime.now().isoformat(),
            "next_24h": [],
            "alerts": [],
            "recommendations": []
        }
        
        # تحليل الاتجاهات الحالية
        ph_trend = self.calculate_trend(historical_data[-5:], "ph")
        moisture_trend = self.calculate_trend(historical_data[-5:], "moisture")
        
        # إنشاء تنبؤات
        current_time = datetime.now()
        for hour in range(0, 25, 3):  # كل 3 ساعات
            prediction_time = current_time + timedelta(hours=hour)
            
            # التنبؤ بناءً على الاتجاهات
            predicted_ph = self.predict_value(current_data["ph"], ph_trend, hour)
            predicted_moisture = self.predict_value(current_data["moisture"], moisture_trend, hour)
            
            # تحليل المخاطر
            risks = self.assess_risks(predicted_ph, predicted_moisture, hour)
            
            predictions["next_24h"].append({
                "time": prediction_time.strftime("%Y-%m-%d %H:%M"),
                "ph": round(predicted_ph, 2),
                "moisture": round(predicted_moisture, 1),
                "risks": risks,
                "action_required": len(risks) > 0
            })
            
            # إضافة تنبيهات إذا لزم الأمر
            if "CRITICAL" in risks:
                predictions["alerts"].append(f"🚨 خطر حرج متوقع عند الساعة {prediction_time.hour}:00")
        
        # إضافة توصيات
        if predictions["alerts"]:
            predictions["recommendations"].append("🔧 فحص النظام فوراً")
        
        if ph_trend == "INCREASING" and current_data["ph"] > 7:
            predictions["recommendations"].append("💧 خفض مستوى pH بالماء الحمضي")
        
        if moisture_trend == "DECREASING" and current_data["moisture"] < 40:
            predictions["recommendations"].append("🌧️ زيادة الري قريباً")
        
        # حفظ التنبؤات
        with open(self.predictions_file, 'w') as f:
            json.dump(predictions, f, indent=2)
        
        return predictions
    
    def predict_value(self, current_value, trend, hours_ahead):
        """تنبؤ بقيمة معينة"""
        # نموذج تنبؤ مبسط
        if trend == "INCREASING":
            return current_value + (hours_ahead * 0.05)
        elif trend == "DECREASING":
            return current_value - (hours_ahead * 0.03)
        else:
            return current_value + np.random.uniform(-0.1, 0.1)
    
    def assess_risks(self, ph, moisture, hour):
        """تقييم المخاطر"""
        risks = []
        
        # تقييم pH
        if ph < 5.5 or ph > 8.0:
            risks.append("CRITICAL_PH")
        elif ph < 6.0 or ph > 7.5:
            risks.append("WARNING_PH")
        
        # تقييم الرطوبة
        if moisture < 20:
            risks.append("CRITICAL_DRY")
        elif moisture < 35:
            risks.append("WARNING_DRY")
        elif moisture > 85:
            risks.append("CRITICAL_WET")
        elif moisture > 75:
            risks.append("WARNING_WET")
        
        # تقييم الوقت (الليل أكثر خطورة)
        if 22 <= hour <= 6 and "CRITICAL" in str(risks):
            risks.append("NIGHT_CRITICAL")
        
        return risks
    
    def display_predictions(self, predictions):
        """عرض التنبؤات"""
        print("\n" + "="*60)
        print("🤖 نظام التنبؤ الذكي - AI Prediction System")
        print("="*60)
        print(f"📅 تم إنشاء التنبؤات في: {predictions['generated_at']}")
        
        if predictions['alerts']:
            print("\n🚨 **تنبيهات مستقبلية:**")
            for alert in predictions['alerts']:
                print(f"   • {alert}")
        
        if predictions['recommendations']:
            print("\n💡 **توصيات استباقية:**")
            for rec in predictions['recommendations']:
                print(f"   • {rec}")
        
        print("\n📊 **تنبؤات الـ 24 ساعة القادمة:**")
        print("-"*60)
        print("الوقت       | pH   | الرطوبة | المخاطر")
        print("-"*60)
        
        for pred in predictions['next_24h']:
            risk_icon = "⚠️ " if pred['risks'] else "✅"
            print(f"{pred['time'][11:16]} | {pred['ph']:4.1f} | {pred['moisture']:6.1f}% | {risk_icon} {', '.join(pred['risks'][:2])}")
        
        print("="*60)

if __name__ == "__main__":
    # مثال على الاستخدام
    ai = AIPredictor()
    
    # بيانات تاريخية وهمية
    historical_data = [
        {"ph": 6.8, "moisture": 65, "temperature": 24, "timestamp": "2026-01-11T10:00:00"},
        {"ph": 7.0, "moisture": 62, "temperature": 25, "timestamp": "2026-01-11T13:00:00"},
        {"ph": 7.2, "moisture": 58, "temperature": 26, "timestamp": "2026-01-11T16:00:00"},
        {"ph": 7.4, "moisture": 55, "temperature": 27, "timestamp": "2026-01-11T19:00:00"},
        {"ph": 7.6, "moisture": 52, "temperature": 26, "timestamp": "2026-01-11T22:00:00"}
    ]
    
    # تدريب النموذج
    model = ai.train_model(historical_data)
    print(f"[✓] تم تدريب النموذج في: {model['trained_at']}")
    
    # التنبؤ
    current_data = {"ph": 7.8, "moisture": 48, "temperature": 28}
    predictions = ai.predict_next_24h(current_data, historical_data)
    
    # عرض النتائج
    ai.display_predictions(predictions)
