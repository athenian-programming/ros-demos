# ROS Demos

## Demos

* [Topic Basics](topic_basics/)
* [Robot Steering rqt plugin](docs/robot_steering.md)
* [Keyboard Teleop](docs/keyboard_teleop.md)
* [XBox Teleop](xbox_teleop/)
* [Joystick Teleop](docs/joystick_teleop.md)
* [Euclid Teleop](euclid_teleop/)
* [IMU Teleop](imu_teleop/)
* [Program Teleop](program_teleop/)
* [RViz Viewer](docs/rviz.md)
* [TurtleBot3 with Gazebo](docs/gazebo_demo.md)
* [SLAM](docs/slam.md)


## Setup

Install the demo packages with:

```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/athenian-robotics/ros-demos.git
```

Add these statements (replacing ubuntu1 with your Ubuntu PC hostname) to your *~/.bashrc*:
```bash
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash

export TURTLEBOT3_MODEL=burger
export ROS_HOSTNAME=ubuntu1.local
export ROS_MASTER_URI=http://ubuntu2.local:11311
```

Build the catkin enviroment with:
```bash
$ cd ~/catkin_ws
$ catkin_make
```

Every machine connecting to *roscore* must have *ROS_MASTER_URI* set appropriately.

More setup details are [here](docs/setup.md).

Run *roscore* on your Ubuntu PC with:
```bash
$ roscore
```



