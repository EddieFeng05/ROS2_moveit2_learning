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
## CH3 Create a URDF for a 6-axis Robotic Arm

### Ch3-1 Intro

### Ch3-2 Create a Description Package

1. New a ros2_ws folder and add src/ folder in ros_ws

2. New package in src/

```
ros2 pkg create my_robot_description

```

3. Setup the my_robot_description package

3.1 Remove the include/ src/ folder

```
rm -r include/ src/
```

3.2 New urdf/ launch/ rviz/ folder

```
mkdir urdf launch rviz
```

* Sample
```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws/src$ ls
my_robot_description
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws/src$ cd my_robot_description/
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description$ ls
CMakeLists.txt  include  package.xml  src
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description$ rm -r include/ src/
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description$ mkdir urdf launch rviz
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description$ ls
CMakeLists.txt  launch  package.xml  rviz  urdf
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description$ 

```

4. Add new code in CMakeList.txt

```

install(
  DIRECTORY launch rviz urdf
  DESTINATION share/${PROJECT_NAME}
)

```

5. Colcon build check your setting is correct

```
colcon build --packages-select my_robot_description 

# This is for build one package. 
```

### 3-3 First Link - Create and Set Up the URDF

1. New arm.urdf

ros2_ws/src/my_robot_description/urdf/arm.urdf

2. Install urdf tutorial (This sample version is jazzy)

```
sudo apt install ros-jazzy-urdf-tutorial

```

3. Test and open URDF file

```
ros2 launch urdf_tutorial display.launch.py model:=/home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/arm.urdf

ros2 launch urdf_tutorial display.launch.py model:=URDF_file_path
```

4. You can learn more about link

https://wiki.ros.org/urdf/XML/link
