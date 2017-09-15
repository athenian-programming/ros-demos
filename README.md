# ROS Demos

## Demos

* [TurtleBot3 Keyboard Control](docs/tb3_keyboard.md)
* [TurtleBot3 with Gazebo](docs/gazebo_demo.md)
* [Topic Basics](topic_basics/)
* [Topic Remapping](topic_remapper/)


## Installation

Install the demo packages with:

```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/athenian-robotics/ros-demos.git
$ cd ~/catkin_ws
$ catkin_make
```

## Setup

Add these statements (replacing ubuntu1 with your Ubuntu PC hostname) to your *.bashrc*:
```bash
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash

export TURTLEBOT3_MODEL=burger
export ROS_HOSTNAME=ubuntu1.local
export ROS_MASTER_URI=http://ubuntu1.local:11311
```

Every machine connecting to *roscore* must have *ROS_MASTER_URI* set appropriately.

More setup details are [here](docs/setup.md).

Run *roscore* on your Ubuntu PC with:
```bash
$ roscore
```



