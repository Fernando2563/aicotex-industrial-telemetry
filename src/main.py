import time

from sensor_block import SensorBlock
from control_block import ControlBlock


def main():
    temp_sensor = SensorBlock(name="Temperature", unit="°C")
    controller = ControlBlock(setpoint=25.0)

    while True:
        value = temp_sensor.read()
        cooling_on = controller.process(value)

        print(f"[Telemetry] {temp_sensor.name}: {value} {temp_sensor.unit}")
        print(f"[Control] Setpoint: {controller.setpoint} | Cooling ON: {cooling_on}")
        print("-" * 50)

        time.sleep(2)


if __name__ == "__main__":
    main()
