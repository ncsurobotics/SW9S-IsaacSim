import numpy as np

from isaacsim.core.prims import SingleXFormPrim
from .oceansim_uw_camera import UW_Camera

from .config import DemoConfig


def _setup_uw_camera(prim_path: str, resolution: tuple[int, int], cfg: DemoConfig):
    cam = UW_Camera(
        prim_path=prim_path,
        resolution=list(resolution),
    )
    cam.initialize(
        UW_param=cfg.uw_params,
        UW_yaml_path=cfg.uw_yaml_path,
        viewport=True,
    )
    cam.set_clipping_range(0.1, 100.0)
    return cam


def setup_sensors(cfg: DemoConfig):
    sensors = {}

    if cfg.use_stereo:
        # Create left/right cameras under the ZED prim
        left_cam = _setup_uw_camera(cfg.left_cam_prim, cfg.resolution, cfg)
        right_cam = _setup_uw_camera(cfg.right_cam_prim, cfg.resolution, cfg)

        # Offset left/right cameras by half-baseline on X
        half = cfg.stereo_baseline_m * 0.5
        SingleXFormPrim(prim_path=cfg.left_cam_prim).set_local_pose(translation=np.array([-half, 0.0, 0.0]))
        SingleXFormPrim(prim_path=cfg.right_cam_prim).set_local_pose(translation=np.array([half, 0.0, 0.0]))

        sensors["left_cam"] = left_cam
        sensors["right_cam"] = right_cam
        print("Stereo UW cameras initialized.")
    else:
        sensors["mono_cam"] = _setup_uw_camera(cfg.left_cam_prim, cfg.resolution, cfg)
        print("Mono UW camera initialized.")

    return sensors
