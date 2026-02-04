import numpy as np
from pxr import PhysxSchema

from isaacsim.core.prims import SingleRigidPrim, SingleGeometryPrim, SingleXFormPrim
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.stage import create_new_stage, add_reference_to_stage
from isaacsim.core.utils.rotations import euler_angles_to_quat
from isaacsim.core.utils.viewports import set_camera_view

from .config import DemoConfig


def setup_scene(cfg: DemoConfig):
    create_new_stage()

    if cfg.scene_usd:
        add_reference_to_stage(usd_path=cfg.scene_usd, prim_path=cfg.scene_prim)
        print(f"Loaded scene USD: {cfg.scene_usd}")
    else:
        print("No scene USD provided; using empty stage.")

    # Load robot
    add_reference_to_stage(usd_path=cfg.robot_usd, prim_path=cfg.robot_prim)
    print(f"Loaded robot USD: {cfg.robot_usd}")

    # Apply PhysX settings to robot
    rob_prim = get_prim_at_path(cfg.robot_prim)
    rob_rigid_api = PhysxSchema.PhysxRigidBodyAPI.Apply(rob_prim)
    rob_rigid_api.CreateDisableGravityAttr(True)
    rob_rigid_api.GetLinearDampingAttr().Set(cfg.robot_linear_damping)
    rob_rigid_api.GetAngularDampingAttr().Set(cfg.robot_angular_damping)

    rob_collider = SingleGeometryPrim(prim_path=cfg.robot_prim, collision=True)
    rob_collider.set_collision_approximation("boundingCube")
    SingleRigidPrim(prim_path=cfg.robot_prim, mass=cfg.robot_mass)

    # Load ZED model under robot and set relative transform
    add_reference_to_stage(usd_path=cfg.zed_usd, prim_path=cfg.zed_prim)
    zed_xform = SingleXFormPrim(prim_path=cfg.zed_prim)
    zed_xform.set_local_pose(
        translation=cfg.zed_translation,
        orientation=euler_angles_to_quat(cfg.zed_rotation_deg, degrees=True),
    )
    print(f"Loaded ZED USD: {cfg.zed_usd}")

    # Set camera view for GUI
    set_camera_view(eye=cfg.camera_eye, target=rob_collider.get_world_pose()[0])

    return cfg.robot_prim
