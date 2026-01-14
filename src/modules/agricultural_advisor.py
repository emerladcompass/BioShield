#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
المساعد الزراعي الذكي - نسخة محسنة بالخوارزمية الواقعية
"""

class AgriculturalAdvisor:
    def __init__(self):
        # قاعدة معرفة المحاصيل
        self.crop_knowledge_base = {
            "قمح": {
                "اسم_علمي": "Triticum aestivum",
                "pH_optimal": (6.0, 7.0),
                "moisture_optimal": (40, 60),
                "temperature_optimal": (15, 24),
                "الأهمية_النسبية": {"ph": 0.35, "moisture": 0.40, "temperature": 0.25}
            },
            "أرز": {
                "اسم_علمي": "Oryza sativa",
                "pH_optimal": (5.0, 6.5),
                "moisture_optimal": (60, 80),
                "temperature_optimal": (20, 35),
                "الأهمية_النسبية": {"ph": 0.30, "moisture": 0.50, "temperature": 0.20}
            },
            "طماطم": {
                "اسم_علمي": "Solanum lycopersicum",
                "pH_optimal": (6.0, 6.8),
                "moisture_optimal": (50, 70),
                "temperature_optimal": (18, 27),
                "الأهمية_النسبية": {"ph": 0.30, "moisture": 0.45, "temperature": 0.25}
            },
            "ذرة": {
                "اسم_علمي": "Zea mays",
                "pH_optimal": (5.8, 7.0),
                "moisture_optimal": (50, 70),
                "temperature_optimal": (21, 30),
                "الأهمية_النسبية": {"ph": 0.35, "moisture": 0.40, "temperature": 0.25}
            },
            "بطاطس": {
                "اسم_علمي": "Solanum tuberosum",
                "pH_optimal": (5.0, 6.0),
                "moisture_optimal": (60, 75),
                "temperature_optimal": (15, 20),
                "الأهمية_النسبية": {"ph": 0.40, "moisture": 0.40, "temperature": 0.20}
            }
        }
        
        self.supported_crops = list(self.crop_knowledge_base.keys())
    
    def _calculate_parameter_score(self, value, optimal_range, is_moisture=False):
        """حساب نقاط معيار واحد"""
        min_val, max_val = optimal_range
        
        if min_val <= value <= max_val:
            return 100  # مثالي
        
        # حساب الانحراف
        if value < min_val:
            deviation = min_val - value
        else:
            deviation = value - max_val
        
        # خصم متدرج (الرطوبة أكثر حساسية)
        if is_moisture:
            if deviation <= 5:
                return 70
            elif deviation <= 10:
                return 50
            elif deviation <= 15:
                return 30
            else:
                return 10
        else:  # pH ودرجة الحرارة
            if deviation <= 0.5:
                return 80
            elif deviation <= 1.0:
                return 60
            elif deviation <= 1.5:
                return 40
            else:
                return 20
    
    def calculate_suitability_score(self, soil_data, crop_info):
        """خوارزمية واقعية لحساب ملاءمة التربة"""
        
        ph = soil_data.get("ph", 7.0)
        moisture = soil_data.get("moisture", 50)
        temperature = soil_data.get("temperature", 22)
        
        # حساب نقاط كل معيار
        ph_score = self._calculate_parameter_score(ph, crop_info["pH_optimal"])
        moisture_score = self._calculate_parameter_score(moisture, crop_info["moisture_optimal"], is_moisture=True)
        temp_score = self._calculate_parameter_score(temperature, crop_info["temperature_optimal"])
        
        # الأهمية النسبية لكل معيار
        weights = crop_info.get("الأهمية_النسبية", {"ph": 0.35, "moisture": 0.40, "temperature": 0.25})
        
        # حساب النتيجة النهائية
        total_score = (ph_score * weights["ph"]) + (moisture_score * weights["moisture"]) + (temp_score * weights["temperature"])
        
        # تصنيف النتيجة
        if total_score >= 85:
            return f"ممتازة ({total_score:.0f}%)", total_score
        elif total_score >= 70:
            return f"جيدة جداً ({total_score:.0f}%)", total_score
        elif total_score >= 55:
            return f"مقبولة ({total_score:.0f}%)", total_score
        elif total_score >= 40:
            return f"ضعيفة ({total_score:.0f}%)", total_score
        else:
            return f"غير مناسبة ({total_score:.0f}%)", total_score
    
    def analyze_for_crop(self, soil_data, crop_type="قمح"):
        """تحليل التربة لمحصول معين"""
        
        if crop_type not in self.supported_crops:
            return {"error": f"المحصول '{crop_type}' غير مدعوم"}
        
        crop_info = self.crop_knowledge_base[crop_type]
        
        # حساب الملاءمة باستخدام الخوارزمية المحسنة
        suitability, score = self.calculate_suitability_score(soil_data, crop_info)
        
        # التوصيات
        recommendations = self._generate_recommendations(soil_data, crop_info, crop_type)
        
        # التحذيرات
        warnings = self._generate_warnings(soil_data, crop_info, crop_type, score)
        
        return {
            "المحصول": crop_type,
            "الاسم_العلمي": crop_info["اسم_علمي"],
            "الملاءمة": suitability,
            "الدرجة": score,
            "التوصيات": recommendations,
            "التحذيرات": warnings,
            "تفاصيل_التربة": {
                "pH": f"{soil_data.get('ph', 0):.2f} (المثالي: {crop_info['pH_optimal'][0]}-{crop_info['pH_optimal'][1]})",
                "الرطوبة": f"{soil_data.get('moisture', 0)}% (المثالي: {crop_info['moisture_optimal'][0]}-{crop_info['moisture_optimal'][1]}%)",
                "الحرارة": f"{soil_data.get('temperature', 0)}°C (المثالي: {crop_info['temperature_optimal'][0]}-{crop_info['temperature_optimal'][1]}°C)"
            }
        }
    
    def _generate_recommendations(self, soil_data, crop_info, crop_type):
        """توليد توصيات مخصصة"""
        recommendations = []
        
        ph = soil_data.get("ph", 7.0)
        moisture = soil_data.get("moisture", 50)
        temperature = soil_data.get("temperature", 22)
        
        ph_min, ph_max = crop_info["pH_optimal"]
        moisture_min, moisture_max = crop_info["moisture_optimal"]
        temp_min, temp_max = crop_info["temperature_optimal"]
        
        # توصيات pH
        if ph < ph_min - 1.0:
            recommendations.append(f"إضافة مواد قلوية لرفع pH بشكل كبير ليكون أنسب لـ{crop_type}")
        elif ph < ph_min:
            recommendations.append(f"إضافة كميات قليلة من المواد القلوية لرفع pH ليكون أنسب لـ{crop_type}")
        elif ph > ph_max + 1.0:
            recommendations.append(f"إضافة مواد حمضية لخفض pH بشكل كبير ليكون أنسب لـ{crop_type}")
        elif ph > ph_max:
            recommendations.append(f"إضافة كميات قليلة من المواد الحمضية لخفض pH ليكون أنسب لـ{crop_type}")
        
        # توصيات الرطوبة
        if moisture < moisture_min - 15:
            recommendations.append(f"زيادة الري بشكل كبير - الرطوبة منخفضة جداً لـ{crop_type}")
        elif moisture < moisture_min:
            recommendations.append(f"زيادة الري بشكل معتدل - الرطوبة منخفضة لـ{crop_type}")
        elif moisture > moisture_max + 15:
            recommendations.append(f"تقليل الري بشكل كبير - الرطوبة مرتفعة جداً لـ{crop_type}")
        elif moisture > moisture_max:
            recommendations.append(f"تقليل الري بشكل معتدل - الرطوبة مرتفعة لـ{crop_type}")
        
        # توصيات الحرارة
        if temperature < temp_min - 5:
            recommendations.append(f"حماية كاملة من البرد - الحرارة منخفضة جداً لـ{crop_type}")
        elif temperature < temp_min:
            recommendations.append(f"حماية جزئية من البرد - الحرارة منخفضة لـ{crop_type}")
        elif temperature > temp_max + 5:
            recommendations.append(f"التبريد الفوري - الحرارة مرتفعة جداً لـ{crop_type}")
        elif temperature > temp_max:
            recommendations.append(f"التبريد المعتدل - الحرارة مرتفعة لـ{crop_type}")
        
        return recommendations
    
    def _generate_warnings(self, soil_data, crop_info, crop_type, score):
        """توليد تحذيرات مخصصة"""
        warnings = []
        
        if score < 40:
            warnings.append(f"⚠️ غير مناسب لـ{crop_type} - يحتاج تحسينات كبيرة")
        elif score < 55:
            warnings.append(f"⚠️ مناسب جزئياً لـ{crop_type} - يحتاج تحسينات متوسطة")
        
        ph = soil_data.get("ph", 7.0)
        moisture = soil_data.get("moisture", 50)
        
        if ph < 5.0 or ph > 8.0:
            warnings.append("⚠️ مستوى pH خارج النطاق الآمن للزراعة")
        
        if moisture < 30:
            warnings.append("⚠️ الرطوبة منخفضة جداً - خطر جفاف التربة")
        elif moisture > 85:
            warnings.append("⚠️ الرطوبة مرتفعة جداً - خطر تعفن الجذور")
        
        return warnings
    
    def compare_crops(self, soil_data):
        """مقارنة ملاءمة جميع المحاصيل"""
        results = {}
        for crop in self.supported_crops:
            analysis = self.analyze_for_crop(soil_data, crop)
            results[crop] = {
                "الملاءمة": analysis["الملاءمة"],
                "الدرجة": analysis["الدرجة"],
                "التقييم": analysis["الملاءمة"].split(" ")[0]
            }
        
        # تحديد أفضل المحاصيل
        best_crops = sorted(
            [(crop, data["الدرجة"]) for crop, data in results.items()],
            key=lambda x: x[1],
            reverse=True
        )
        
        top_crops = [crop for crop, score in best_crops if score >= 55][:3]
        
        return {
            "جميع_النتائج": results,
            "أفضل_المحاصيل": top_crops,
            "الترتيب_المفصل": best_crops,
            "ملخص": f"أفضل {len(top_crops)} محصول لهذه التربة: {', '.join(top_crops)}"
        }
    
    def get_crop_list(self):
        """الحصول على قائمة المحاصيل المدعومة"""
        return self.supported_crops

# اختبار مباشر
if __name__ == "__main__":
    print("🧪 اختبار AgriculturalAdvisor المحسن")
    print("="*50)
    
    advisor = AgriculturalAdvisor()
    
    # بيانات اختبارية
    test_soil = {"ph": 6.5, "moisture": 55, "temperature": 22}
    
    print(f"📊 بيانات التربة: pH={test_soil['ph']}, رطوبة={test_soil['moisture']}%")
    print(f"🌱 المحاصيل المدعومة: {', '.join(advisor.get_crop_list())}")
    
    # مقارنة المحاصيل
    print("\n🔍 مقارنة المحاصيل:")
    comparison = advisor.compare_crops(test_soil)
    
    for crop, data in comparison["جميع_النتائج"].items():
        icon = "⭐" if crop in comparison["أفضل_المحاصيل"] else "✓"
        print(f"   {icon} {crop}: {data['الملاءمة']}")
    
    print(f"\n🎯 {comparison['ملخص']}")
    
    # تحليل مفصل لأفضل محصول
    if comparison["أفضل_المحاصيل"]:
        best_crop = comparison["أفضل_المحاصيل"][0]
        print(f"\n📋 تحليل مفصل لـ{best_crop}:")
        analysis = advisor.analyze_for_crop(test_soil, best_crop)
        
        print(f"   الاسم العلمي: {analysis['الاسم_العلمي']}")
        print(f"   الملاءمة: {analysis['الملاءمة']}")
        
        if analysis['التوصيات']:
            print(f"   التوصيات:")
            for rec in analysis['التوصيات'][:2]:
                print(f"     • {rec}")
        
        if analysis['التحذيرات']:
            print(f"   التحذيرات:")
            for warning in analysis['التحذيرات']:
                print(f"     ⚠️ {warning}")
