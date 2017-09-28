# IMU Teleop 

## Description

The *imu_teleop.py* program subscribes to */realsense/odom* and publishes Twist values to
*/cmd_vel*. 

The */realsense/odom* values are:
* Linear: */realsense/odom/pose/pose/orientation/y* 
* Angular: */realsense/odom/pose/pose/orientation/z*


## Usage

Goto the [Scenarios](http://euclid.local/#config/scenarios) on the Euclid and launch the *6DOF* scenario.

Run *imu_teleop.py* with: 
```bash
# On Ubunutu PC
$ rosrun imu_teleop imu_teleop.py
```

Launch a robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
# On Ubuntu PC
$ rosrun turtlesim turtlesim_node /turtle1/cmd_vel:=/cmd_vel
# On Ubuntu PC
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```