---
layout: default
title: API Reference
permalink: /api
---

# API Reference

## Main Modules

### src/main.py
Main entry point with CLI interface.

### src/core/engine.py
Core system engine.

### src/modules/
All functional modules:

- soil_monitor.py - Soil monitoring
- auto_adjuster.py - Auto-adjustment
- ai_predictor.py - AI predictions
- report_generator.py - Report generation
- live_dashboard.py - Live dashboard

## Configuration API

Location: config/config.json

Key parameters:
- Soil targets (pH, moisture)
- AI settings
- Monitoring intervals
