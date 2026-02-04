from .control import ManualController


class Scenario:
    def __init__(self, robot_prim_path: str, sensors: dict, manual_control: bool = True):
        self._sensors = sensors
        self._manual_control = manual_control
        self._controller = ManualController(robot_prim_path) if manual_control else None

    def update(self, dt: float):
        if self._controller:
            self._controller.apply()

        for sensor in self._sensors.values():
            # UW_Camera renders one frame per call
            sensor.render()

    def cleanup(self):
        if self._controller:
            self._controller.cleanup()
        for sensor in self._sensors.values():
            sensor.close()
