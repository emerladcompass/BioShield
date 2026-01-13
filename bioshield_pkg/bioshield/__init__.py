"""
BioShield - Intelligent Soil Health Monitoring System
=====================================================

Version: 3.3.0
Author: Samir Baladi
Email: emerladcompass@gmail.com
"""

__version__ = "3.3.0"
__author__ = "Samir Baladi"
__email__ = "emerladcompass@gmail.com"

# إعادة تصدير الوظائف الرئيسية
def run():
    """تشغيل النظام الرئيسي."""
    from .main import main
    return main()

def adjust():
    """تشغيل نظام التعديل."""
    from .run_auto_adjust import main as adjust_main
    return adjust_main()

# إعادة تصدير الكلاسات الرئيسية
from .modules.soil_monitor import SoilMonitor
from .modules.auto_adjuster import SoilAutoAdjuster
from .modules.report_generator import ReportGenerator

__all__ = [
    "run",
    "adjust",
    "SoilMonitor",
    "SoilAutoAdjuster",
    "ReportGenerator",
    "__version__",
    "__author__",
]
