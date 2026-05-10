# Adam-pro_robotera

This repository contains PNDbotics model files for simulation and control, including URDF/MJCF descriptions, mesh assets, and related resources.

[中文](#中文) | [English](#english)

---

## 中文

本仓库主要包含以下机器人模型资产：

- `adam_pro_robotera/`
  - `adam_pro.urdf`
  - `adam_pro.xml`
  - `adam_pro_obj.xml`
  - `adam_pro_main.xml`
  - `scene_adam_pro.xml`
  - `meshes_stl/`
  - `meshes_dae/`
  - `assets/`

- `adam_pro/`
  - `adam_pro.urdf`
  - `adam_pro.xml`
  - `adam_pro_obj.xml`
  - `adam_pro_main.xml`
  - `scene_adam_pro.xml`
  - 相关网格资产目录

- `adam_pro_hand/`
  - `adam_pro.urdf`
  - `adam_pro.xml`
  - `adam_pro_main.xml`
  - `adam_pro_obj.xml`
  - `scene_adam_pro.xml`
  - `meshes_stl/`
  - `meshes_dae/`
  - `meshes_stl_0.25/`
  - `assets/`

- `XHAND1_URDF_ver 1.3/`
  - `xhand1_left/urdf/xhand_left.urdf`
  - `xhand1_right/urdf/xhand_right.urdf`
  - `xhand1_left/meshes/`
  - `xhand1_right/meshes/`

### adam_pro_hand 主被动自由度说明

`adam_pro_hand/` 中的手部模型已经补充为主被动自由度结构，行为与 `E:\TeleVision\assets\inspire_hand` 的联动方式保持大体一致。

- 拇指：
  - `thumb_MCP_joint1` 作为独立主自由度保留。
  - `thumb_MCP_joint2` 作为拇指屈伸主关节。
  - `thumb_PIP_joint` 跟随 `thumb_MCP_joint2`，倍率为 `1.6`。
  - `thumb_DIP_joint` 跟随 `thumb_MCP_joint2`，倍率为 `2.4`。

- 食指、中指、无名指、小指：
  - `MCP` 为主关节。
  - `DIP` 为从关节，按 `1.0` 倍跟随对应 `MCP`。

- URDF 中：
  - 通过 `mimic` 建立主从关系。

- MuJoCo XML 中：
  - 通过 `equality/joint` 建立与 URDF 一致的主被动耦合关系。
  - 仅主关节保留驱动，从动关节不单独施加控制。

### 来源与致谢

本仓库当前内容基于 [pndbotics/pnd_models](https://github.com/pndbotics/pnd_models) 构建和整理。

感谢 PNDbotics 公司提供原始模型、资源与相关基础工作。

---

## English

This repository mainly contains the following robot model assets:

- `adam_pro_robotera/`
  - `adam_pro.urdf`
  - `adam_pro.xml`
  - `adam_pro_obj.xml`
  - `adam_pro_main.xml`
  - `scene_adam_pro.xml`
  - `meshes_stl/`
  - `meshes_dae/`
  - `assets/`

- `adam_pro/`
  - `adam_pro.urdf`
  - `adam_pro.xml`
  - `adam_pro_obj.xml`
  - `adam_pro_main.xml`
  - `scene_adam_pro.xml`
  - related mesh asset folders

- `adam_pro_hand/`
  - `adam_pro.urdf`
  - `adam_pro.xml`
  - `adam_pro_main.xml`
  - `adam_pro_obj.xml`
  - `scene_adam_pro.xml`
  - `meshes_stl/`
  - `meshes_dae/`
  - `meshes_stl_0.25/`
  - `assets/`

- `XHAND1_URDF_ver 1.3/`
  - `xhand1_left/urdf/xhand_left.urdf`
  - `xhand1_right/urdf/xhand_right.urdf`
  - `xhand1_left/meshes/`
  - `xhand1_right/meshes/`

### adam_pro_hand Active-Passive DOF Notes

The hand model in `adam_pro_hand/` has been updated with coupled active-passive finger DOFs, following the same overall linkage idea as `E:\TeleVision\assets\inspire_hand`.

- Thumb:
  - `thumb_MCP_joint1` remains an independent active DOF.
  - `thumb_MCP_joint2` is the main thumb flexion joint.
  - `thumb_PIP_joint` follows `thumb_MCP_joint2` with a multiplier of `1.6`.
  - `thumb_DIP_joint` follows `thumb_MCP_joint2` with a multiplier of `2.4`.

- Index, middle, ring, and pinky fingers:
  - `MCP` is the active joint.
  - `DIP` is the passive joint, following the corresponding `MCP` at `1.0x`.

- In URDF:
  - The coupling is defined with `mimic`.

- In MuJoCo XML:
  - The same coupling is defined with `equality/joint`.
  - Only the active joints keep actuators, while passive joints are not driven independently.

### Attribution

This repository is built and organized based on [pndbotics/pnd_models](https://github.com/pndbotics/pnd_models).

Special thanks to PNDbotics for the original models, assets, and foundational work.
