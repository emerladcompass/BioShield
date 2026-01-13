"""
BioShield Termux Package
=======================
إصدار معدل للعمل على Termux
"""
__version__ = "3.3.0"
__author__ = "Samir Baladi"

# إعادة تصدير الوظائف الرئيسية
def run():
    """تشغيل النظام الرئيسي."""
    from .main import main
    return main()

def adjust():
    """تشغيل نظام التعديل."""
    from .run_auto_adjust import main as adjust_main
    return adjust_main()

# استيراد الكلاسات الرئيسية للتصدير
try:
    from .modules.soil_monitor import SoilMonitor
    from .modules.auto_adjuster import SoilAutoAdjuster
    from .modules.report_generator import ReportGenerator
except ImportError:
    # للتوافق
    pass

__all__ = ['run', 'adjust', 'SoilMonitor', 'SoilAutoAdjuster', 'ReportGenerator']
