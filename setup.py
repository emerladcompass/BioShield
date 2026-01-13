#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="bioshield",
    version="3.3.5",
    author="Samir Baladi",
    author_email="emerladcompass@gmail.com",
    description="BioShield: Intelligent Soil Health Monitoring & Adjustment System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emerladcompass/BioShield",
    
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=6.0.0",
        "python-dateutil>=2.8.0",
    ],
    
    extras_require={
        "full": [
            "numpy>=1.21.0",
            "pandas>=1.3.0",
            "scipy>=1.7.0",
            "networkx>=2.6.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "twine>=4.0.0",
            "wheel>=0.37.0",
        ],
    },
    
    entry_points={
        "console_scripts": [
            "bioshield = bioshield.main:main",
            "bs-adjust = bioshield.run_auto_adjust:main",
        ],
    },
    
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Android",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Agriculture",
    ],
    
    keywords=["agriculture", "soil", "ai", "monitoring", "termux"],
)
