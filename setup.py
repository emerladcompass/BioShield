#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

# تحديد الحزم يدوياً
packages = [
    'bioshield_termux',
    'bioshield_termux.core_engine',
    'bioshield_termux.modules',
    'bioshield_termux.network',
]

setup(
    name="bioshield",
    version="3.3.1",
    author="Samir Baladi",
    author_email="emerladcompass@gmail.com",
    description="Intelligent Soil Health Monitoring System for Termux",
    
    # استخدام packages بدلاً من find_packages
    packages=packages,
    
    # تحديد مسارات الحزم
    package_dir={
        'bioshield_termux': 'src',
        'bioshield_termux.core_engine': 'src/core_engine',
        'bioshield_termux.modules': 'src/modules',
        'bioshield_termux.network': 'src/network',
    },
    
    # تبعيات خفيفة
    install_requires=[
        'pyyaml>=5.4.0',
        'python-dateutil>=2.8.0',
    ],
    
    # إدخالات سطر الأوامر - باستخدام المسارات الصحيحة
    entry_points={
        'console_scripts': [
            'bioshield = bioshield_termux.main:main',
            'bs-adjust = bioshield_termux.run_auto_adjust:main',
        ],
    },
    
    # معلومات إضافية
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: Android',
    ],
    
    python_requires='>=3.8',
)
