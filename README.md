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

# 🎯 PASSO 2 — Agora vamos melhorar o SensorBlock

Seu `sensor_block.py` está vazio.  
Substitua por isso:

```python
import random

class SensorBlock:
    """
    Industrial sensor abstraction layer.
    Simulates temperature sensor behavior.
    """

    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

    def read(self) -> float:
        """
        Simulate sensor reading.
        Replace with Modbus / OPC-UA / BACnet in real application.
        """
        return round(random.uniform(22.0, 30.0), 2)
import json
import time

class TelemetryBlock:
    """
    Telemetry layer responsible for formatting
    and publishing structured industrial data.
    """

    def __init__(self, system_name: str):
        self.system_name = system_name

    def build_payload(self, sensor_data: dict, control_data: dict) -> str:
        payload = {
            "system": self.system_name,
            "timestamp": int(time.time()),
            "sensor": sensor_data,
            "control": control_data
        }
        return json.dumps(payload, indent=2)

    def publish(self, payload: str):
        """
        Currently prints to console.
        Future: MQTT / Cloud / Database integration.
        """
        print(payload)
        print("-" * 60)
