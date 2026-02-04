# ZED UW Standalone Demo

This standalone script set launches an Isaac Sim GUI session, loads your scene + robot USD, attaches the ZED model, and renders underwater camera output (mono or stereo) with keyboard control.

## Run
From your Isaac Sim install root, run:

```bash
./python.sh -m standalone.zed_uw_example.main \
  --scene-usd /path/to/scene.usd \
  --robot-usd /home/sidgupta4761/aquapack/SWIX-sim-v2/SWIX-sim-v2.usd \
  --zed-usd /home/sidgupta4761/aquapack/zed-isaac-sim/usd/ZED_XM.usdc
```

## Convenience wrapper
You can also run the wrapper which sets `PYTHONPATH` for you:

```bash
./standalone/zed_uw_example/run.sh \
  --scene-usd /path/to/scene.usd \
  --robot-usd /home/sidgupta4761/aquapack/SWIX-sim-v2/SWIX-sim-v2.usd \
  --zed-usd /home/sidgupta4761/aquapack/zed-isaac-sim/usd/ZED_XM.usdc
```

If your Isaac Sim root is not the default, set it like:

```bash
ISAAC_ROOT=/path/to/isaac-sim ./standalone/zed_uw_example/run.sh ...
```

If you want mono instead of stereo:

```bash
./python.sh -m standalone.zed_uw_example.main --mono
```

To use underwater params saved from the Color Picker extension:

```bash
./python.sh -m standalone.zed_uw_example.main --uw-yaml /path/to/render_param.yaml
```

## Controls
- W/S/A/D: planar thrust
- Arrow Up/Down: rise/sink
- J/L: yaw
- I/K: pitch
- Left/Right arrows: roll

## Notes
- ZED transform relative to robot is set in `config.py`.
- Stereo cameras are created as OceanSim UW camera prims under the ZED prim. If you want to use real ZED camera prims, update `left_cam_prim` / `right_cam_prim` in `config.py` to match your USD.
