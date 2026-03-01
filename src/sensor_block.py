import random


class SensorBlock:
    """
    Sensor abstraction layer.
    Simulates industrial temperature sensor.
    """

    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

    def read(self) -> float:
        """
        Simulates reading from a real sensor.
        Replace this with Modbus / OPC-UA / BACnet in production.
        """
        return round(random.uniform(20.0, 30.0), 2)
        
