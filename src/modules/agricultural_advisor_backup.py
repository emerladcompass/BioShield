#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
المساعد الزراعي الذكي - نسخة مبسطة للبدء
"""

class AgriculturalAdvisor:
    def __init__(self):
        self.crops = ["قمح", "أرز", "طماطم", "ذرة", "بطاطس"]
        self.base_knowledge = {
            "قمح": {"pH_min": 6.0, "pH_max": 7.0, "moisture_min": 40, "temperature_optimal": "15-24°C"},
            "أرز": {"pH_min": 5.0, "pH_max": 6.5, "moisture_min": 60, "temperature_optimal": "20-35°C"},
            "طماطم": {"pH_min": 6.0, "pH_max": 6.8, "moisture_min": 50, "temperature_optimal": "18-27°C"}
        }
    
    def analyze_for_crop(self, soil_data, crop_type="قمح"):
        """تحليل التربة لمحصول معين"""
        if crop_type not in self.crops:
            return {"error": f"المحصول '{crop_type}' غير مدعوم"}
        
        # تحليل مبسط
        ph = soil_data.get("ph", 7.0)
        moisture = soil_data.get("moisture", 50)
        
        crop_info = self.base_knowledge.get(crop_type, {})
        
        # حساب الملاءمة البسيطة
        if crop_info:
            ph_ok = crop_info["pH_min"] <= ph <= crop_info["pH_max"]
            moisture_ok = moisture >= crop_info["moisture_min"]
            
            if ph_ok and moisture_ok:
                suitability = "ممتازة"
            elif ph_ok or moisture_ok:
                suitability = "جيدة"
            else:
                suitability = "تحتاج تحسين"
        else:
            suitability = "غير معروف"
        
        # توصيات مبسطة
        recommendations = []
        if ph < 6.0:
            recommendations.append("إضافة مواد قلوية لرفع درجة الحموضة")
        if moisture < 50:
            recommendations.append("زيادة الري")
        
        return {
            "المحصول": crop_type,
            "التوصيات": recommendations,
            "الملاءمة": suitability,
            "تفاصيل_التربة": {
                "pH": f"{ph:.1f}",
                "الرطوبة": f"{moisture}%",
                "الحرارة": f"{soil_data.get('temperature', 25)}°C"
            }
        }
    
    def compare_crops(self, soil_data):
        """مقارنة المحاصيل"""
        results = {}
        for crop in self.crops[:3]:  # أول 3 محاصيل فقط
            analysis = self.analyze_for_crop(soil_data, crop)
            results[crop] = analysis["الملاءمة"]
        
        # تحديد أفضل المحاصيل
        best_crops = [crop for crop, score in results.items() 
                     if score in ["ممتازة", "جيدة"]]
        
        return {
            "جميع_النتائج": results,
            "أفضل_المحاصيل": best_crops,
            "ملخص": f"أفضل {len(best_crops)} محصول: {', '.join(best_crops)}"
        }
    
    def get_crop_list(self):
        """الحصول على قائمة المحاصيل المدعومة"""
        return self.crops

# اختبار مباشر
if __name__ == "__main__":
    print("🧪 اختبار AgriculturalAdvisor")
    print("="*50)
    
    advisor = AgriculturalAdvisor()
    
    # بيانات تربة افتراضية
    test_soil = {"ph": 6.5, "moisture": 55, "temperature": 22}
    
    print(f"📊 بيانات التربة: pH={test_soil['ph']}, رطوبة={test_soil['moisture']}%")
    print(f"🌱 المحاصيل المدعومة: {', '.join(advisor.get_crop_list())}")
    
    # تحليل محصول معين
    analysis = advisor.analyze_for_crop(test_soil, "قمح")
    print(f"\n📋 تحليل القمح:")
    print(f"   الملاءمة: {analysis['الملاءمة']}")
    print(f"   التوصيات: {', '.join(analysis['التوصيات']) if analysis['التوصيات'] else 'لا توجد'}")
    
    # مقارنة المحاصيل
    print("\n🔍 مقارنة المحاصيل:")
    comparison = advisor.compare_crops(test_soil)
    for crop, suitability in comparison["جميع_النتائج"].items():
        print(f"   {crop}: {suitability}")
    
    print(f"\n🎯 {comparison['ملخص']}")
