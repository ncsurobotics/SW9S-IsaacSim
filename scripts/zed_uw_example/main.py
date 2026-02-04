import argparse
import os
import sys

from omni.isaac.kit import SimulationApp

def _find_repo_root(start_dir: str) -> str | None:
    cur = os.path.abspath(start_dir)
    for _ in range(6):
        if os.path.isdir(os.path.join(cur, "isaacsim", "oceansim")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return None


# Ensure OceanSim repo is importable
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = _find_repo_root(THIS_DIR) or os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.append(REPO_ROOT)


def _parse_args():
    parser = argparse.ArgumentParser(description="OceanSim UW Camera + ZED standalone demo")
    parser.add_argument("--scene-usd", type=str, default=None, help="Path to scene USD")
    parser.add_argument("--robot-usd", type=str, default=None, help="Path to robot USD")
    parser.add_argument("--zed-usd", type=str, default=None, help="Path to ZED USD")
    parser.add_argument("--uw-yaml", type=str, default=None, help="Path to underwater render YAML")
    parser.add_argument("--mono", action="store_true", help="Use mono camera instead of stereo")
    parser.add_argument("--res", type=int, nargs=2, default=None, help="Camera resolution W H")
    return parser.parse_args()


def main():
    args = _parse_args()

    simulation_app = SimulationApp({"headless": False})

    # Import omni + repo modules after SimulationApp is created
    import omni.timeline
    from .config import DemoConfig
    from .scene_setup import setup_scene
    from .sensors_setup import setup_sensors
    from .scenario import Scenario

    cfg = DemoConfig()
    cfg.scene_usd = args.scene_usd
    if args.robot_usd:
        cfg.robot_usd = args.robot_usd
    if args.zed_usd:
        cfg.zed_usd = args.zed_usd
    if args.uw_yaml:
        cfg.uw_yaml_path = args.uw_yaml
    if args.res:
        cfg.resolution = tuple(args.res)
    cfg.use_stereo = not args.mono

    robot_prim_path = setup_scene(cfg)
    sensors = setup_sensors(cfg)
    scenario = Scenario(robot_prim_path, sensors, manual_control=True)

    timeline = omni.timeline.get_timeline_interface()
    timeline.play()

    dt = 1.0 / 60.0
    try:
        while simulation_app.is_running():
            scenario.update(dt)
            simulation_app.update()
    finally:
        scenario.cleanup()
        simulation_app.close()


if __name__ == "__main__":
    main()
