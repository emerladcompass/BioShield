from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bioshield",
    version="1.0.0",
    author="Samir Baladi",
    author_email="emerladcompass@gmail.com",
    description="BioShield: Intelligent Soil Monitoring & Auto-Adjustment System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emerladcompass/BioShield",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.4.0",
        "requests>=2.26.0",
    ],
    keywords=[
        "agriculture", 
        "soil-monitoring", 
        "ai", 
        "machine-learning",
        "environmental-science",
    ],
)
