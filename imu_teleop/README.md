# IMU Teleop 

## Description

The *imu_teleop.py* program subscribes to */realsense/odom* and publishes Twist values to
*/cmd_vel*. 

The */realsense/odom* values are:
* Linear: */realsense/odom/pose/pose/orientation/y* 
* Angular: */realsense/odom/pose/pose/orientation/z*


## Usage

Goto the [Scenarios](http://euclid.local/#config/scenarios) on the Euclid and launch the *6DOF* scenario.

Launch the TurtleBot3 operation packages and enable the robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Run *imu_teleop.py* with: 
```bash
# On Ubunutu PC
$ rosrun imu_teleop imu_teleop.py
```

