# IMU Teleop 

## Usage

Launch the TurtleBot3 operation packages and enable the robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Goto the [Scenarios](http://euclid.local/#config/scenarios) on the Euclid and launch the *6DOF* scenario.

Run *imu_teleop.py* with: 
```bash
# On Ubunutu PC
$ rosrun imu_teleop imu_teleop.py
```

This program subscribes to two topics:
* Linear: */realsense/odom/pose/pose/orientation/y*
* Angular: */realsense/odom/pose/pose/orientation/z*