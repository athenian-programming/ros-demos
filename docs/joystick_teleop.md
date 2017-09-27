# Joystick Teleop

## Setup

Install the necessary packages with:
````bash
# On Ubunutu PC
$ sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
````

## Usage

Launch a [teleop_twist_joy](http://wiki.ros.org/teleop_twist_joy) node with: 
```bash
# On Ubuntu PC
$ roslaunch teleop_twist_joy teleop.launch joy_dev:=/dev/input/js1
```

Launch the TurtleBot3 operation packages and enable the robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

