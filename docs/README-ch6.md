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


### Ch6-3 Start Everything From the Terminal

1. Terminal 1

```
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro /home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro)"

```
2. Terminal 2

```
ros2 run controller_manager ros2_control_node --params-file /home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_bringup/config/ros2_controllers.yaml

```

* Still have some error

### Ch6-4 Activity 04 - Write the Launch File

### Ch6-5 Activity 04 - Solution

1. New a launch file

ros2_ws/src/my_robot_bringup/launch/my_robot.launch.xml

2. Write the code in launch file

3. Add exec_depend pkg in package.xml

ros2_ws/src/my_robot_bringup/package.xml

4. Build code and Launch file

```
colcon build && source install/setup.bash
```

```
ros2 launch my_robot_bringup my_robot.launch.xml 
```

5. Add MotionPlanning and use ompl in rviz

6. Save as rviz config in config folder

ros2_ws/src/my_robot_bringup/config/my_robot_moveit.rviz

7. Adjust the rviz path in launch file

ros2_ws/src/my_robot_bringup/launch/my_robot.launch.xml

8. Launch file again and try plan & execute the robot


```
colcon build && source install/setup.bash
```

```
ros2 launch my_robot_bringup my_robot.launch.xml 
```
