import time

from sensor_block import SensorBlock
from control_block import ControlBlock
from telemetry_block import TelemetryBlock


def main():
    temp_sensor = SensorBlock(name="Temperature", unit="°C")
    controller = ControlBlock(setpoint=25.0)
    telemetry = TelemetryBlock(system_name="Aicotex Industrial Telemetry")

    while True:
        value = temp_sensor.read()
        cooling_on = controller.process(value)

        payload = telemetry.build_payload(
            sensor_data={
                "name": temp_sensor.name,
                "value": value,
                "unit": temp_sensor.unit
            },
            control_data={
                "setpoint": controller.setpoint,
                "cooling_on": cooling_on
            }
        )

        telemetry.publish(payload)

        time.sleep(2)


if __name__ == "__main__":
    main()
