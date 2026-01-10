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
First Link-Create and Set Up URDF
1. New arm.urdf

ros2_ws/src/my_robot_description/urdf/arm.urdf

2. Install urdf tutorial (This sample version is jazzy)

```
sudo apt install ros-jazzy-urdf-tutorial

```

3. Test and open URDF file

```
ros2 launch urdf_tutorial display.launch.py model:=/home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/arm.urdf

#ros2 launch urdf_tutorial display.launch.py model:=URDF_file_path
```

4. You can learn more about link

https://wiki.ros.org/urdf/XML/link

### 3-4 Second link - Recap of the Process to Add Links Together
Second link Recap and Add Links Together
1. Add shoulder_link and joint1 in arm.urdf

/ros2_ws/src/my_robot_description/urdf/arm.urdf

2. Adjust the parmeter in link and joint. 

3. Test code

```
ros2 launch urdf_tutorial display.launch.py model:=/home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/arm.urdf


#ros2 launch urdf_tutorial display.launch.py model:=URDF_file_path
```

### 3-5 Activity 01 - Finish the URDF for the Arm

* Build the 6 axis robotic arm

Specifications for the 6-axis robotic arm:
Links:
- base_link (box size 0.4 0.4 0.1)
- shoulder_link (cylinder len 6.5 radius 6.1)
- arm_link (cylinder len 0.6 radius 0.05)
- elbow link (cylinder len 6.1 radius 8.05)
- forearm link (cylinder len 6.5 radius 0.05)
- wrist_link (box size 0.1 0.1 0.05)
- hand_link (box size 0.1 0.1 0.02)
- tool_link (no visual)
Joints:
- joint1 (revolute, axis z, min -3.14, max 3.14)
- joint2 (revolute, axis y, min 6, max 2.5)
- joint3 (revolute, axis y, min 0, max 2.5)
- joint4 (revolute, axis z, min -3.14, max 3.14)
- joint5 (revolute, axis y, min -1.57, max 1.57)
- joint6 (continuous, axis z)
- hand_tool_joint (fixed)

### 3-6 Activity 01 - Solution

1. Follow the robot spec, make URDF. 
Specifications for the 6-axis robotic arm:
Links:
-Ibase_link (box size 0.4 0.4 0.1)
- shoulder_link (cylinder len 6.5 radius 6.1)
- arm_link (cylinder len 0.6 radius 0.05)
- elbow link (cylinder len 6.1 radius 8.05)
- forearm link (cylinder len 6.5 radius 0.05)
- wrist_link (box size 0.1 0.1 0.05)
- hand_link (box size 0.1 0.1 0.02)
- tool_link (no visual)
Joints:
- joint1 (revolute, axis z, min -3.14, max 3.14)
- joint2 (revolute, axis y, min 6, max 2.5)
- joint3 (revolute, axis y, min 0, max 2.5)
- joint4 (revolute, axis z, min -3.14, max 3.14)
- joint5 (revolute, axis y, min -1.57, max 1.57)
- joint6 (continuous, axis z)
- hand_tool_joint (fixed)

2. Test code

```
ros2 launch urdf_tutorial display.launch.py model:=/home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/arm.urdf


#ros2 launch urdf_tutorial display.launch.py model:=URDF_file_path
```

### 3-7 Improve the URDF with Xacro

1. New file my_robot.urdf.xacro

ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro

2. New file common_properties.xacro for common properties

ros2_ws/src/my_robot_description/urdf/common_oproperties.xacro

3. New file arm.xacro

ros2_ws/src/my_robot_description/urdf/arm.xacro

4. Add include file in my_robot.urdf.xacro

ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro

5. Test code

```
ros2 launch urdf_tutorial display.launch.py model:=/home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro

#ros2 launch urdf_tutorial display.launch.py model:=URDF_file_path
```

### 3-8 Create a Launch File to Display the Robot

1. Check the node list when launch urdf_tutorial display.launch.py

* Terminaal 1
```
ros2 launch urdf_tutorial display.launch.py model:=/home/eddie/Documents/ROS2_moveit2_learning/ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro

#ros2 launch urdf_tutorial display.launch.py model:=URDF_file_path
```


* Terminal 2
```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning$ ros2 node list
/joint_state_publisher
/robot_state_publisher
/rviz
/transform_listener_impl_5cba80b3bc80
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning$ 

```

2. New launch file

ros2_ws/src/my_robot_description/launch/display.launch.xml

3. Test launch file, remember you are in ros2_ws folder

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
* Notice: You just see blank in rviz windwos, you need to setup config. 

4. Setting rviz

Step1. Global Options/Fixed Frame: map -->  base_link
Step2. Add RobotMode
Step3. RobotMode/Description Topic :/robot_description
Step4. Add TF 

When you finish 4 steps you will see 6 axis robotic arm with TF in rviz windows. Next step:

Step5. Save as Rviz config in your rviz folder

ros2_ws/src/my_robot_description/rviz/urdf_config.rviz

5. Add new code about rviz config in launch file

ros2_ws/src/my_robot_description/launch/display.launch.xml

6. Test launch file, remember you are in ros2_ws folder

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

* Notice: You see robot in rviz windows like you setup in your rivz config. 