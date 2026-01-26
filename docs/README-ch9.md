# ROS 2 - Moveit 2 - Control a Robotic Arm

This is follow course about "ROS 2 - Moveit 2 - Control a Robotic Arm.

https://www.udemy.com/course/ros2-moveit2/?couponCode=CP250105G1

## The environment setup

* Ubuntu 24.04
* Ros2 Jazzy
* Updat your environment

```
sudo apt update
sudo apt upgrade
```

* Install ros2-control and ros2-controllers(In this case is Jazzy)

```
sudo apt install ros-jazzy-ros2-control ros-jazzy-ros2-controllers
```

----
## CH9 Connect Moveit to the Hardware

### Ch9-1 Intro

### Ch9-2 ros2_control Quick Recap and the Hardware I Will Use

### Ch9-3 my_robot_hardware Package Overview

1. Create package my_robot_hardware

ros2_ws/src/my_robot_hardware

```
ros2 pkg create my_robot_hardware
```

2. Add motor driver library

ros2_ws/src/my_robot_hardware/include/my_robot_hardware/xl330_driver.hpp

3. Add arm_hardware_interface.hpp

ros2_ws/src/my_robot_hardware/include/my_robot_hardware/arm_hardware_interface.hpp

4. Add arm_hardware_interface.cpp

ros2_ws/src/my_robot_hardware/src/arm_hardware_interface.cpp

5. Add my_robot_hardware_interface.xml

ros2_ws/src/my_robot_hardware/my_robot_hardware_interface.xml

6. Adjust content about CMakeList.txt

ros2_ws/src/my_robot_hardware/CMakeLists.txt

7. Build code, you should download dynmixel-sdk first.

```
sudo apt install ros-jazzy-dynamixel-sdk

colcon build --packages-select my_robot_hardware 

```

### Ch9-4 Use the Hardware Interface in the URDF

1. Add ros2_control name gripper in my_robot.ros2_control.xacro

ros2_ws/src/my_robot_description/urdf/my_robot.ros2_control.xacro

2. Change the plugin for name Arm and add param(motor id and port) in my_robot.ros2_control.xacro

3. Build and Run

* Terminal 1: Joint1 and joint2 the angle follow the real motors

```
colcon build

ros2 launch my_robot_bringup my_robot.launch.xml

```

* If you have some error you need decrease update_rate (100 -> 20 Hz) in ros2_controller.yaml

ros2_ws/src/my_robot_bringup/config/ros2_controllers.yaml

* Terminal 2

```
ros2 run my_robot_command_cpp commander 
```

* Terminal 3: Watch the real motor move

```
ros2 topic pub -1 /joint_command example_interfaces/msg/Float64MultiArray “{data:[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}"
```