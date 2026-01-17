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
## CH6 Bringup Package

### Ch6-1 Intro

### Ch6-2 Create and Set Up the Bringup Package

1. Create new package named my_robot_bringup

```
ros2 pkg create my_robot_bringup
```

2. Clean the package

```
rm -r include/ src/
mkdir launch config

```

3. Write the code in CMakeList.txt

```
install(
  DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)
```

4. Copy the "ros2_ws/src/my_robot_moveit_config/config/ros2_controllers.yaml" to "ros2_ws/src/my_robot_bringup/config/"

5. Copy the "ros2_ws/src/my_robot_moveit_config/config/my_robot.ros2_control.xacro" to "ros2_ws/src/my_robot_description/urdf/my_robot.ros2_control.xacro"

6. Write the include code in my_robot.urdf.xacro

ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro

7. Change code in my_robot.ros2_control.xacro

ros2_ws/src/my_robot_description/urdf/my_robot.ros2_control.xacro