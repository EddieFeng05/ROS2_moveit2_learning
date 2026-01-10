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
## CH4 Set Up Your Robot for MoveIT

### Ch4-1 Intro

### Ch4-2 Activity 02 - Add Collision Tags

Collision tags will be the same as visual, but sometimes we will change collision for reduce the calculation.

ex. 
a. cylinder --> box
b. mash(from stl) --> box

### Ch4-3 Activity 02 - Solution

1. Add collsion tags for every link.

ex. 
a. cylinder --> box
b. mash(from stl) --> box

2. Test launch file, remember you are in ros2_ws folder

* Step 1
```
colcon build 
```

* Step 2 
```
source install/setup.bash 
```

* Step 3
```
ros2 launch my_robot_description display.launch.xml 
```