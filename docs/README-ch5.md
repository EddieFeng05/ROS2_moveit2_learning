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
## CH5 Add a Gripper to the Arm

### Ch5-1 Intro

### Ch5-2 Create a URDF for a Gripper

1. New a gripper.xacro

ros2_ws/src/my_robot_description/urdf/gripper.xacro

2. Add gripper_base_link, gripper_left_finger_link and gripper_right_finger_link

3. Add joints

4. Run and test

```
ros2 launch urdf_tutorial display.launch.py model:=/home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/gripper.xacro
```

### Ch5-3 Connect the Gripper to the Arm

1. Adjust code in gripper.xacro

1.1 delete name

1.2 cut matrerial codes and paste that in common_properties.xacro

ros2_ws/src/my_robot_description/urdf/common_properties.xacro
ros2_ws/src/my_robot_description/urdf/gripper.xacro

2. Add new code in my_robot.urdf.xacro

2.1 include gripper.xacro

2.2 Add joint to connnect tool_link and gripper_base_link

ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro

3. Run and test

```
ros2 launch my_robot_description display.launch.xml 
```

4. See the tf tree

```
ros2 run tf2_tools view_frames 
```