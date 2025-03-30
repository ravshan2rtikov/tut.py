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

    def change_speed(self, value):
        self._change_speed = value
        print("Speed Changed")

    # 0 is clockwise rotation, 1 is anti clockwise rotation
    def change_direction(self, value):
        self._change_dir = value
        print("Rotate diraction changed")


fan = motor(0, 0, 0, 0)
print("Start button is: ", fan._start_button)
fan.turn_on()
print("Start button is: ", fan._start_button)
fan.turn_off()
print("Stopbutton is: ", fan._stop_button)

fan.change_speed(50)
print(fan._change_speed)

fan.change_direction(1)
print(fan._change_dir)
