import json
import time


class TelemetryBlock:
    """
    Telemetry Layer
    Responsible for formatting and publishing data.
    """

    def __init__(self, system_name: str):
        self.system_name = system_name

    def build_payload(self, sensor_data: dict, control_data: dict) -> str:
        payload = {
            "system": self.system_name,
            "timestamp": time.time(),
            "sensor": sensor_data,
            "control": control_data,
        }
        return json.dumps(payload, indent=2)

    def publish(self, payload: str):
        # For now, just print (future: MQTT / Cloud / Database)
        print("[Telemetry Publish]")
        print(payload)
        print("=" * 60)
