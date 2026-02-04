# Standalone demo config for OceanSim UW camera + ZED model

from dataclasses import dataclass, field
import numpy as np


@dataclass
class DemoConfig:
    # USD paths provided by user
    scene_usd: str | None = None
    robot_usd: str = "/home/sidgupta4761/aquapack/SWIX-sim-v2/SWIX-sim-v2.usd"
    zed_usd: str = "/home/sidgupta4761/aquapack/zed-isaac-sim/usd/ZED_XM.usdc"

    # Prim paths
    world_prim: str = "/World"
    scene_prim: str = "/World/scene"
    robot_prim: str = "/World/rob"
    zed_prim: str = "/World/rob/zed"

    # ZED transform relative to robot (rounded from screenshot)
    zed_translation: np.ndarray = field(default_factory=lambda: np.array([0.0, -0.548, -0.034]))
    zed_rotation_deg: np.ndarray = field(default_factory=lambda: np.array([0.0, 0.0, -90.0]))

    # UW camera settings
    use_stereo: bool = True
    resolution: tuple[int, int] = (1280, 720)
    left_cam_prim: str = "/World/rob/zed/uw_left"
    right_cam_prim: str = "/World/rob/zed/uw_right"
    stereo_baseline_m: float = 0.12  # approximate ZED X Mini baseline

    # UW render params
    uw_yaml_path: str | None = None
    uw_params: np.ndarray = field(default_factory=lambda: np.array([0.0, 0.31, 0.24, 0.05, 0.05, 0.2, 0.05, 0.05, 0.05]))

    # Robot dynamics
    robot_mass: float = 5.0
    robot_linear_damping: float = 10.0
    robot_angular_damping: float = 10.0

    # Camera view for the GUI
    camera_eye: np.ndarray = field(default_factory=lambda: np.array([5.0, 0.6, 0.4]))
