class HallSensor:
    def __init__(self, pin=None):
        self.pin = pin
        self._rpm = 0.0

    def read_rpm(self) -> float:
        return self._rpm  # replace with real GPIO read later
