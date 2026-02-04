# SW9S-IsaacSim
Software and assets related to Isaac Sim simulation of the SW9 platform

### Environment

Hardware: AMD Ryzen 7950X3D, NVIDIA RTX 5070 ti

OS/Drivers: Ubuntu 24.04, kernel 6.14.0-29-generic, nvidia-driver-570-open 570.195.03, CUDA 12.8

Software: Isaac Sim 5.0.0, ZED SDK 5.1 for Ubuntu 24 (CUDA 12 - TensorRT 10), ZED Isaac Sim Extension 4.1.0

### Structure

assets/env/RectPoolScene and assets/env/OceanSim\_assets contain useful stuff for constructing stage, and assets/robot and assets/zed_usds contain assets for robot and camera. 

stages/testing/minimal\_zed\_v2, stages/testing/oceansim\_rectpoolscene\_example.usd, and stages/testing/unity\_sim\_env.usd are testing stages/environments, and stages/main/RectPoolScene.usd and stages/main/SWIX-stage-v1.usd contain more relevant stages. 

scripts/standalone contains Isaac Python scripts, Warp, and general Python scripts. It is primarily being tested for OceanSim integration with Isaac Python.

### Notes

Many paths are probably broken, especially in scripts, since I reorganized and didn't fix the paths, they will be of varying difficulty to fix

Isaac Sim 5.0.0 is used since OceanSim isn't tested to be reliable with newer versions like 5.1.0+

scripts/zed\_uw\_example contains a set of test scripts for integrating OceanSim with Isaac Python, right now all it can do is load a blank stage and crash


