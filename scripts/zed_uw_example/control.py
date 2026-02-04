import numpy as np
from pxr import Gf, PhysxSchema

from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.oceansim.utils.keyboard_cmd import keyboard_cmd


class ManualController:
    def __init__(self, robot_prim_path: str):
        self._robot_prim = get_prim_at_path(robot_prim_path)
        self._force_api = PhysxSchema.PhysxForceAPI.Apply(self._robot_prim)

        self._force_cmd = keyboard_cmd(
            base_command=np.array([0.0, 0.0, 0.0]),
            input_keyboard_mapping={
                "W": [10.0, 0.0, 0.0],
                "S": [-10.0, 0.0, 0.0],
                "A": [0.0, 10.0, 0.0],
                "D": [0.0, -10.0, 0.0],
                "UP": [0.0, 0.0, 10.0],
                "DOWN": [0.0, 0.0, -10.0],
            },
        )
        self._torque_cmd = keyboard_cmd(
            base_command=np.array([0.0, 0.0, 0.0]),
            input_keyboard_mapping={
                "J": [0.0, 0.0, 10.0],
                "L": [0.0, 0.0, -10.0],
                "I": [0.0, -10.0, 0.0],
                "K": [0.0, 10.0, 0.0],
                "LEFT": [-10.0, 0.0, 0.0],
                "RIGHT": [10.0, 0.0, 0.0],
            },
        )

    def apply(self):
        force_cmd = Gf.Vec3f(*self._force_cmd._base_command)
        torque_cmd = Gf.Vec3f(*self._torque_cmd._base_command)
        self._force_api.CreateForceAttr().Set(force_cmd)
        self._force_api.CreateTorqueAttr().Set(torque_cmd)

    def cleanup(self):
        self._force_cmd.cleanup()
        self._torque_cmd.cleanup()
