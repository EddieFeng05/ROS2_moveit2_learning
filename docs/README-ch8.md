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
## CH8 Interact with Moveit using the Python API

### Ch8-1 Intro

### Ch8-2 Make the Arm Move with the MoveIt Python API

1. Install moveit python library

```
sudo apt install ros-jazzy-moveit-py

```


2. Create a new package

ros2_ws/src/my_robot_command_py

```
ros2 pkg create my_robot_command_py --build-type ament_python --dependencies rclpy

```

3. New the test_moveit.py and paste the sample code

ros2_ws/src/my_robot_command_py/my_robot_command_py/test_moveit.py


4. Add library in test_moveit.py

5. Write the initial in main

6. Write robot move

7. Add the node in setup.py

ros2_ws/src/my_robot_command_py/setup.py

8. Build and Run

* Terminal 1

a. Build 

```
colcon build --packages-select my_robot_command_py --symlink-install
```


b. Launch code

```
ros2 launch my_robot_bringup my_robot.launch.xml

```

* Terminal 2

```
ros2 run my_robot_command_py test_moveit

```

### Ch8-3 Joint and Pose Goal - Python

* In Python library, we cannot use cartesian_path

We add Joint and Pose template, you can try yourself.

1. Install tf-transformations library 

```
sudo apt install ros-jazzy-tf-transformations -y
```

2. Build and run code

* Terminal 1

```
colcon build --packages-select my_robot_command_py --symlink-install

ros2 launch my_robot_bringup my_robot.launch.xml
```

* Terminal 2

```
ros2 run my_robot_command_py test_moveit

```


### Ch8-4 Integrate the Python API inside an OOP Node

1. New a file commander_template.py

ros2_ws/src/my_robot_command_py/my_robot_command_py/commander_template.py

2. Make a file executable

```
chmod +x commander_template.py 
```

3. Write code in commander_template.py