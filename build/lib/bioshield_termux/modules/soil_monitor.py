#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class SoilMonitor:
    """محاكاة قراءة بيانات التربة"""
    def simulate_sensor_reading(self):
        return {
            "ph": round(random.uniform(6.4, 7.5), 2),
            "moisture": random.randint(33, 90),
            "temperature": random.randint(18, 28)
        }
