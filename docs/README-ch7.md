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
## CH7 Interact with Moveit using the C++ API

### Ch7-1 Intro

### Ch7-2 Make the Arm Move with the MoveIt C++ API

1. Create new package named my_robot_command_cpp

```
ros2 pkg create my_robot_command_cpp --build-type ament_cmake --dependencies rclcpp

```

2. New cpp file in command_cpp/src , and wirte the ros2 sturcture.

```
ros2_ws/src/my_robot_command_cpp/src/test_moveit.cpp
```

3. New about moveit code in test_moveit.cpp

4. Add new code in CMakeList.txt

ros2_ws/src/my_robot_command_cpp/CMakeLists.txt

5. Add new code in packages.xml

ros2_ws/src/my_robot_command_cpp/package.xml

6. Build and Launch code

* Terminal 1
```
colcon build --packages-select my_robot_command_cpp 

ros2 launch my_robot_bringup my_robot.launch.xml 

```
* Terminal 2
```
ros2 run my_robot_command_cpp test_moveit 

```

7. Extention: Add new arm pose(home) and add gripper group. 

### Ch7-3 Joint and Pose Goal - C++

1. Commment out Named goal code in test_moveit.cpp

ros2_ws/src/my_robot_command_cpp/src/test_moveit.cpp

2. Add Joint Goal

3. Build and Launch code

* Terminal 1
```
colcon build --packages-select my_robot_command_cpp 

ros2 launch my_robot_bringup my_robot.launch.xml 

```
* Terminal 2
```
ros2 run my_robot_command_cpp test_moveit 

```

4. Commment out Joint goal code in test_moveit.cpp

ros2_ws/src/my_robot_command_cpp/src/test_moveit.cpp

5. Add Pose Goal

6. Build and Launch code

* Terminal 1
```
colcon build --packages-select my_robot_command_cpp 

ros2 launch my_robot_bringup my_robot.launch.xml 

```
* Terminal 2
```
ros2 run my_robot_command_cpp test_moveit 

```