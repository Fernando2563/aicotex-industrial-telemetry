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
# Aicotex Industrial Telemetry

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Architecture](https://img.shields.io/badge/Architecture-Modular-green)
![Industry](https://img.shields.io/badge/Domain-Industrial%20IoT-orange)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)

Modular industrial telemetry and intelligent monitoring platform developed in Python.

Designed for industrial environments, OT/IT integration, edge computing, and future cloud connectivity.

---

## Overview

Aicotex is a layered industrial telemetry architecture structured into independent modules:

- **Sensor Layer** – Data acquisition abstraction
- **Control Layer** – Logic processing and decision engine
- **Telemetry Layer** – Structured JSON data publishing
- **Integration Layer (Future)** – MQTT / Cloud / Database connectivity
- **Intelligence Layer (Future)** – Edge AI anomaly detection

The system simulates a temperature control environment but is architected for real-world industrial automation, data centers, and mission-critical infrastructure.

---

## Architecture Diagram
           +-----------------------+
           |      Cloud Layer      |
           |  (Azure / AWS / DB)   |
           +-----------+-----------+
                       |
                 MQTT / REST
                       |
           +-----------v-----------+
           |    Telemetry Layer    |
           |   (TelemetryBlock)    |
           +-----------+-----------+
                       |
           +-----------v-----------+
           |     Control Layer     |
           |    (ControlBlock)     |
           +-----------+-----------+
                       |
           +-----------v-----------+
           |     Sensor Layer      |
           |    (SensorBlock)      |
           +-----------------------+
           
---

## Project Structure

---

## Example Telemetry Payload

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
python src/main.py
## Why This Project Matters

Industrial environments are rapidly converging OT (Operational Technology) and IT (Information Technology).

Aicotex is designed to simulate and scale toward real-world industrial telemetry scenarios, including:

- Critical infrastructure monitoring
- Industrial automation systems
- Edge computing environments
- Data center thermal control
- Autonomous systems (AGV / LGV environments)

The architecture is intentionally modular to support:

- Scalability
- Cloud-native integration
- Real-time telemetry streaming
- Edge AI anomaly detection
## Industrial Use Cases

Aicotex architecture can be adapted for:

- Smart factories
- Autonomous logistics systems (LGV / AGV)
- Data centers (thermal and power monitoring)
- Industrial IoT deployments
- Predictive maintenance systems
