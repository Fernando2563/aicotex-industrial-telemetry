# Aicotex Industrial Telemetry

Modular industrial telemetry and intelligent monitoring platform developed in Python.

Designed for industrial environments, OT/IT integration, and scalable cloud connectivity.

---

## Overview

Aicotex is a modular industrial monitoring architecture structured into independent layers:

- **Sensor Layer** – Data acquisition abstraction  
- **Control Layer** – Logic processing and decision engine  
- **Telemetry Layer** – Structured data publishing  
- **Integration Layer (Future)** – MQTT / Cloud / Database connectivity  

The system simulates a temperature control environment but is architected for real-world industrial automation, data centers, and mission-critical infrastructure.

---

## Architecture

### Components

- **SensorBlock**  
  Responsible for sensor abstraction and data acquisition.

- **ControlBlock**  
  Processes sensor input and applies control logic (setpoint-based decision).

- **TelemetryBlock**  
  Formats and publishes structured telemetry payloads (JSON-ready).

---
src/
 ├── main.py
 ├── sensor_block.py
 ├── control_block.py
 └── telemetry_block.py
## Roadmap
- [ ] MQTT integration
- [ ]  MQTT broker integration (Eclipse Mosquitto)
- [ ]  Persistent database storage    
- [ ] Time-series database integration (InfluxDB / PostgreSQL)
- [ ] Edge AI anomaly detection
- [ ] Edge AI anomaly detection (scikit-learn / TensorFlow Lite)
