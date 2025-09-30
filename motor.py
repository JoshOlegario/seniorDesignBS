class Motor:
    def __init__(self):
        self._running = False
        self._duty = 0.0

    def start(self, duty: float = 1.0):
        self._running = True
        self._duty = max(0.0, min(1.0, duty))

    def stop(self):
        self._running = False
        self._duty = 0.0

    def is_running(self) -> bool:
        return self._running
