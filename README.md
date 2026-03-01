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

## Example Telemetry Output

```json
{
  "system": "Aicotex Industrial Telemetry",
  "timestamp": 1700000000,
  "sensor": {
    "name": "Temperature",
    "value": 26.4,
    "unit": "°C"
  },
  "control": {
    "setpoint": 25.0,
    "cooling_on": true
  }
}

---


