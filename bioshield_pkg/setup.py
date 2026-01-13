#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="bioshield",
    version="3.3.0",
    author="Samir Baladi",
    author_email="emerladcompass@gmail.com",
    description="Intelligent Soil Health Monitoring & Adjustment System",
    long_description=open("../README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/emerladcompass/BioShield",
    
    # العثور على جميع الحزم تلقائياً
    packages=find_packages(),
    
    # المتطلبات
    install_requires=[
        "pandas>=1.3.0",
        "scipy>=1.7.0", 
        "networkx>=2.6.0",
        "pyyaml>=5.4.0",
        "python-dateutil>=2.8.0",
    ],
    
    # أوامر CLI
    entry_points={
        "console_scripts": [
            "bioshield = bioshield.main:main",
            "bs-adjust = bioshield.run_auto_adjust:main",
        ],
    },
    
    # التصنيفات
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Android",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Agriculture",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    
    python_requires=">=3.8",
    keywords=["agriculture", "soil", "ai", "monitoring", "automation"],
)
