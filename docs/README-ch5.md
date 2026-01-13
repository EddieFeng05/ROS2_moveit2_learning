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

### 5-4 Activity 03 - Add the Gripper to the MoveIt Config

Load the existing configuration inside the Moveit Setup Assistant. Then, follow those steps and try to make something that works:
1. Re-generate self-collision matrix
2. Add a planning group for the gripper
3. Create a few poses: gripper_open, gripper_closed, gripper_half_closed
4. Add an end effector
5. Add ros2_control state interface for gripper_left_finger_joint
6. Add a ROS 2 and Moveit controller for the gripper (follow joint trajectory)

* Once you‘re done with the configuration, you can re-generate the package, fix the velocity/acceleration limits, and try to launch the demo.launch.py. If you get some errors, try to fix then using the logs. If you can't fix them, no worries, check out the next video for the solution.

### 5-5 Activity 03 - Solution

1. Remember if you open new terminal you must to source setup.bash

```
source install.bash

```
2. Launch code

```
ros2 launch moveit_setup_assistant setup_assistant.launch.py 

```

3. Click Browse and Select your moveit_config folder. Then Load Files.

* If you moveit setup assistant chrash. You can try add some code in you ~/.bashrc
* But you successful rate just 50%.

```
export OGRE_RTT_MODE=Copy
export QT_XCB_GL_INTEGRATION=none
export LIBGL_ALWAYS_SOFTWARE=1

```

4. After suceessful load files, click Generate Collision Matrix

5. Define Planning groups: Add Group: gripper --> Add Joints. Select gripper's links.

6. Robot Poses: Add Pose --> Set open, close, close_hafe.

7. End Effectors: Add End Effector --> gripper

8. ros2_control URDF Modification: Add interfaces

9. ROS2 controllers: Auto Add ...

10. Moveit Controllers: Auto Add ...

11. Configuration Files: Generate Package

12. After genrate finish, you can see about gripper descrption in you code like my_robot.srdf

13. Change parmaemter in joint_limits.yaml

ros2_ws/src/my_robot_moveit_config/config/joint_limits.yaml

``` 
# All joints
has_velocity_limits: true
max_velocity: 1 --> 1.0
has_acceleration_limits: false -->true
max_acceleration: 0 --> 1.0

```

14. Add parmaemter in moveit_controllers.yaml

ros2_ws/src/my_robot_moveit_config/config/moveit_controllers.yaml

```
    action_ns: follow_joint_trajectory
    default: true
```

15. Delete sensors_3d.yaml


16. Build and lanuch code

```
colcon build %% source install/setup.bash
```

```
ros2 launch my_robot_moveit_config demo.launch.py 
```

17. You can planning gripper group.