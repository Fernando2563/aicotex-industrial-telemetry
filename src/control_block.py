class ControlBlock:
    """
    Industrial Control Block
    Implements automation logic similar to PLC function blocks.
    """

    def __init__(self, setpoint: float):
        self.setpoint = setpoint
        self.output = False

    def process(self, input_value: float) -> bool:
        if input_value > self.setpoint:
            self.output = True
        else:
            self.output = False

        return self.output

    def status(self) -> dict:
        return {
            "setpoint": self.setpoint,
            "output": self.output
        }
