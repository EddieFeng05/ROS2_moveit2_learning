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
## CH2 2. Setup and Installation for ROS2 and Moveit2

### Ch2-1 Introv

### Ch2-2 Starting Code + Robot Overview

1. Install Ros2 jazzy, set in ~/.basshrc

```
source /opt/ros/jazzy/setup.bash
```

2. Set colocn_argcomplete, Add new code in ~/.bashrc

```
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

### Ch2-3 Install MoveIt 2

1. Follow the moveit offical website, install the moveit 2. 

https://moveit.ai/install-moveit2/binary

2. Install middleware

2.1 Install software

```
sudo apt install ros-$ROS_DISTRO-rmw-cyclonedds-cpp

```
2.2 Set

```
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

```
2.3 Set middleware, Add new code in ~/.bashrc

```
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```

2.4 Install moveit (sample is jazzy)

```
sudo apt install ros-jazzy-moveit

```

### Ch2-4 Tools for the Course

1. Install VS code (Not recommended in by cli, it's not full installation)

```
sudo snap install code --classic

```

2. Open workspace in the cli by VScode, 

```
code .
```

3. VScode recommnded extension

3.1 Robot Developer Extensions for ROS2

3.2 CMake

4. Install terminator

```
sudo apt install terminator
```

* Command
ctrl + shift + o : Add a new windows at downside

ctrl + shift + o : Add a new windows at rightside

ctrl + shift + o : Delete a windows