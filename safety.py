class Safety:
    def __init__(self, emergency_stop=False):
        self.emergency_stop = emergency_stop

    def set_e_stop(self, state: bool):
        self.emergency_stop = bool(state)

    def ok_to_run(self) -> bool:
        return not self.emergency_stop
