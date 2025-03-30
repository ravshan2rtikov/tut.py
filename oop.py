class motor:
    def __init__(self, start_button, stop_button, change_dir, change_speed):
        self._start_button = start_button
        self._stop_button = stop_button
        self._change_dir = change_dir
        self._change_speed = change_speed

    def turn_on(self):
        if self._stop_button == 1:
            self._stop_button = 0
        self._start_button = True
        print("Motor is ON")

    def turn_off(self):
        if self._start_button == 1:
            self._start_button = 0
        self._stop_button = True
        print("Motor is OFF")
