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

### Ch7-4 Cartesian Path

1. Add the Catesian path code, add pose1(z += -0.2)

ros2_ws/src/my_robot_command_cpp/src/test_moveit.cpp

2. Build and Launch code

* Terminal 1
```
colcon build --packages-select my_robot_command_cpp 

ros2 launch my_robot_bringup my_robot.launch.xml 

```

* You can show the trail

RobotModel/Links/tool_link/Show Trail [v]

RobotModel/All Links Enabled [ ]

TF [ ]


* Terminal 2
```
ros2 run my_robot_command_cpp test_moveit 

```

3. Make trajectory be triangle, add pose2(y += 0.2), pose3(y += -0.2, z += 0.2)

4. Build and Launch code

* Terminal 1
```
colcon build --packages-select my_robot_command_cpp 

ros2 launch my_robot_bringup my_robot.launch.xml 

```

* You can show the trail

RobotModel/Links/tool_link/Show Trail [v]

RobotModel/All Links Enabled [ ]

TF [ ]


* Terminal 2
```
ros2 run my_robot_command_cpp test_moveit 

```

### Ch7-5 Integrate the C++ API inside an OOP node - Setup

1. New a file commander_template.cpp

ros2_ws/src/my_robot_command_cpp

2. Write the ros2 node structure in commander_template.cpp

3. Write the class Commander in commander_template.cpp

4. Write th MoveGroupInterface in commander_template.cpp


### Ch7-6 Integrate the C++ API inside an OOP node - Methods

1. Add void planAndExecute code in class private commander_template.cpp

2. Add void goToNamedTarget code in class public commander_template.cpp

3. Add void goToJointTarget code in class public commander_template.cpp

4. Add void goToPoseTarget code in class public commander_template.cpp

5. Adjust void goToNamedTarget code add cartesian_path flag in class public commander_template.cpp


### Ch7-7 Add a Topic Subscriber

1. Add grpper control in class public the NamedTarget refer by srdf file commander_template.cpp

2. Add topic subscriber and write Condition

3. Add depend in packages.xml

ros2_ws/src/my_robot_command_cpp/package.xml

4. Add node in CMakeList.txt

ros2_ws/src/my_robot_command_cpp/CMakeLists.txt

5. Run code

* Terminal 1

a. Build code 

```
colcon build --packages-select my_robot_command_cpp 
```

b. Launch the bringup

```
ros2 launch my_robot_bringup my_robot.launch.xml

```

* Terminal 2

a. Run the node

```
ros2 run my_robot_command_cpp commander 
```


* Terminal 3

a. check topic list, see thge open_gripper node

```
ros2 topic list
```

```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ ros2 topic list 
/arm_controller/controller_state
/arm_controller/joint_trajectory
/arm_controller/transition_event
/attached_collision_object
/clicked_point
/collision_object
/controller_manager/activity
/controller_manager/introspection_data/full
/controller_manager/introspection_data/names
/controller_manager/introspection_data/values
/controller_manager/statistics/full
/controller_manager/statistics/names
/controller_manager/statistics/values
/diagnostics
/display_contacts
/display_planned_path
/dynamic_joint_states
/goal_pose
/gripper_controller/controller_state
/gripper_controller/joint_trajectory
/gripper_controller/transition_event
/initialpose
/joint_state_broadcaster/transition_event
/joint_states
/monitored_planning_scene
/open_gripper
/parameter_events
/pipeline_state
/planning_scene
/planning_scene_world
/recognized_object_array
/robot_description
/robot_description_semantic
/rosout
/rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/feedback
/rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/update
/tf
/tf_static
/trajectory_execution_event
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ 
```

b. see info about open_grpper

```
ros2 topic info /open_gripper

```

```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ ros2 topic info /open_gripper 
Type: example_interfaces/msg/Bool
Publisher count: 0
Subscription count: 1
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ 

```

c. gripper open and close


```
# close
ros2 topic pub -1 /open_gripper example_interfaces/msg/Bool "{data: false}"

# open
ros2 topic pub -1 /open_gripper example_interfaces/msg/Bool "{data: true}"
```

```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ ros2 topic pub -1 /open_gripper example_interfaces/msg/Bool "{data: false}"
publisher: beginning loop
publishing #1: example_interfaces.msg.Bool(data=False)

eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ ros2 topic pub -1 /open_gripper example_interfaces/msg/Bool "{data: true}"
publisher: beginning loop
publishing #1: example_interfaces.msg.Bool(data=True)

eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ 

```


### Ch7-8 Activity 05 - Add Subscribers for Joint and Pose Commands

### Ch7-9 Activity 05 - Solution [1/2]

1. show the Float64MultiArray

```
ros2 interface show example_interfaces/msg/Float64MultiArray 
```

```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ ros2 interface show example_interfaces/msg/Float64MultiArray 
# This is an example of using complex datatypes.
# It is not recommended to use directly.
# To use a similar datastruct please define a custom message with appropriate semantic meaning.

# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
	#
	#
	#
	#
	#
	MultiArrayDimension[] dim #
		string label   #
		uint32 size    #
		uint32 stride  #
	uint32 data_offset        #
float64[]         data          # array of data
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ 

```

2. Add float_multi_array.hpp and add varialbe in commander_template.cpp

ros2_ws/src/my_robot_command_cpp/src/commander_template.cpp

3. Add new subscription name joint_command and add jointCmdCallback to do goToJointTaget

4. Run code

* Terminal 1

a. Build code 

```
colcon build --packages-select my_robot_command_cpp 
```

b. Launch the bringup

```
ros2 launch my_robot_bringup my_robot.launch.xml

```

* Terminal 2

a. Run the node

```
ros2 run my_robot_command_cpp commander 
```


* Terminal 3

a. check topic list, see thge /joint_command node

```
ros2 topic list
```

```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ ros2 topic list 
/arm_controller/controller_state
/arm_controller/joint_trajectory
/arm_controller/transition_event
/attached_collision_object
/clicked_point
/collision_object
/controller_manager/activity
/controller_manager/introspection_data/full
/controller_manager/introspection_data/names
/controller_manager/introspection_data/values
/controller_manager/statistics/full
/controller_manager/statistics/names
/controller_manager/statistics/values
/diagnostics
/display_contacts
/display_planned_path
/dynamic_joint_states
/goal_pose
/gripper_controller/controller_state
/gripper_controller/joint_trajectory
/gripper_controller/transition_event
/initialpose
/joint_command
/joint_state_broadcaster/transition_event
/joint_states
/monitored_planning_scene
/open_gripper
/parameter_events
/pipeline_state
/planning_scene
/planning_scene_world
/recognized_object_array
/robot_description
/robot_description_semantic
/rosout
/rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/feedback
/rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/update
/tf
/tf_static
/trajectory_execution_event
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ 

```

b. see the info

```
ros2 topic info /joint_command 
```

```
eddie@eddie-VM:~$ ros2 topic info /joint_command 
Type: example_interfaces/msg/Float64MultiArray
Publisher count: 0
Subscription count: 1

```

c. pub joint command

```
ros2 topic pub -1 /joint_command example_interfaces/msg/Float64MultiArray "{data:[0.5, 0.5, 0.5, 0.5, 0.5, 0.5]}"

```

```
eddie@eddie-VM:~/Documents/ROS2_moveit2_learning/ros2_ws$ ros2 topic pub -1 /joint_command example_interfaces/msg/Float64MultiArray "{data: [-0.5, 0.5, 0.5, 0.5, 0.5, 0.5]}"
publisher: beginning loop
publishing #1: example_interfaces.msg.Float64MultiArray(layout=example_interfaces.msg.MultiArrayLayout(dim=[], data_offset=0), data=[-0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
```
### Ch7-10 Activity 05 - Solution [2/2]