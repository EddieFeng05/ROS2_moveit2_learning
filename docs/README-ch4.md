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

### Ch4-4 Run the MoveIt Setup Assistant

1. Launch moveit setup assistant

```
ros2 launch moveit_setup_assistant setup_assistant.launch.py 
```
2. Click Create New MoveIt

3. Click Brows --> Select the .xacro (my_robot.urdf.xacro) --> Load Files

ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro

4. You can check visual / collision

5. Self-Collision: click Generate collision matrix

6. Virtual Joints: Click Add Virtual Joint 

6.1 Virtual Joint Name: vitrual_joint

6.2 JJParent Frame Name: world

6.3 Click Save

7. Planning Groups: Click Add Group

7.1 Group Name: arm

7.2 Kinematic Solver: kdl_kinematics_p....

7.3 Click Add Joints

7.3.1 Available Joints select all joints move to Selected Joints

7.3.2 Save

8. Robot Poses: Click Add Pose

8.1 Pose Name: home / pose_1 / pose_2

8.2 Joint: Up to you

8.3 Save

8.4 Add three pose(home / pose_1 / pose_2)

9. End Effectors: we don't use it in this sample.

10. Passive Joints: we don't use it in this sample.

11. ros2_control URDF Modification:

11.1 Command interfaces: check position

11.2 State Interfaces: check position

11.3 Click interfaces

12. ROS2 controllers: Click Auto Add JointTrajectoryControllers....

13. Moveit Controllers: Click Auto Add FollowJointsTrajectory ....

14. Perception: we don't use it in this sample.

15. Launch Files: we don't use it in this sample.

16. Author information: Write the name and email. If it blank it cannot build.

17. Configuration Files: 

17.1 Click Browse

17.2 select src/  and name xxx_moveit_config

17.3 Gjenerate Package

17.4 It show warn because we don't set end effector, just click ok

17.5 After generate, please check moveit_config folder, if you see succeful exist. You can close the assistant windows.

18. Adjust moveit_config

18.1 Launch moveit_setup_assistant

```
 ros2 launch moveit_setup_assistant setup_assistant.launch.py 
```

18.2 Click Existing Moveit ...

18.3 Browse

18.4 Select xxx_moveit_config folder

18.5 Click Load Files