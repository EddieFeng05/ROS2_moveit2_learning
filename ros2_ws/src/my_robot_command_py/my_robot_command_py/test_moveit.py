#! /usr/bin/env python3
import rclpy
from moveit.planning import MoveItPy
from moveit.planning import PlanningComponent
from moveit_configs_utils import MoveItConfigsBuilder


ROBOT_CONFIG = MoveItConfigsBuilder(robot_name="my_robot", package_name="my_robot_moveit_config")\
                                    .robot_description_semantic("config/my_robot.srdf", {"name": "my_robot"})\
                                    .to_dict()

ROBOT_CONFIG = {
    **ROBOT_CONFIG,
    "planning_scene_monitor": {
            "name": "planning_scene_monitor",
            "robot_description": "robot_description",
            "joint_state_topic": "/joint_states",
            "attached_collision_object_topic": "/moveit_cpp/planning_scene_monitor",
            "publish_planning_scene_topic": "/moveit_cpp/publish_planning_scene",
            "monitored_planning_scene_topic": "/moveit_cpp/monitored_planning_scene",
            "wait_for_initial_state_timeout": 10.0,
        },
        "planning_pipelines": {
            "pipeline_names": ["ompl"]
        },
        "plan_request_params": {
            "planning_attempts": 1,
            "planning_pipeline": "ompl",
            "max_velocity_scaling_factor": 1.0,
            "max_acceleration_scaling_factor": 1.0
        },
        "ompl": {
            "planning_plugins": ["ompl_interface/OMPLPlanner"],
            "request_adapters": ["default_planning_request_adapters/ResolveConstraintFrames",
                                 "default_planning_request_adapters/ValidateWorkspaceBounds",
                                 "default_planning_request_adapters/CheckStartStateBounds",
                                 "default_planning_request_adapters/CheckStartStateCollision"],
            "response_adapters": ["default_planning_response_adapters/AddTimeOptimalParameterization",
                                  "default_planning_response_adapters/ValidateSolution",
                                  "default_planning_response_adapters/DisplayMotionPath"],
            "start_state_max_bounds_error": 0.1
        }
}

def main(args=None):
    rclpy.init(args=args)
    robot = MoveItPy(node_name="moveit_py", config_dict=ROBOT_CONFIG)
    arm: PlanningComponent = robot.get_planning_component("arm")
    gripper: PlanningComponent = robot.get_planning_component("gripper")

    arm.set_start_state_to_current_state()
    arm.set_goal_state(configuration_name="pose_1")
    plan_result = arm.plan()
    if plan_result:
        robot.execute(plan_result.trajectory, controllers=[])

    rclpy.shutdown()