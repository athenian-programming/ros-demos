# XBox Teleop

## Description

The *xbox_teleop.py* program subscribes to */joy* and publishes Twist values to */cmd_vel*.

## Setup

Install the necessary packages with:
````bash
# On Ubunutu PC
$ sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
````

## Usage

Launch the Xbox USB Gamepad Userspace Driver with:
```bash
$ sudo xboxdrv --silent
# If you get a LIBUSB_ERROR_BUSY error, resolve it with:
# sudo rmmod xpad
```

Run *xbox_remapper.launch*, which launches both the xbox_teleop node and 
the [teleop_twist_joy](http://wiki.ros.org/teleop_twist_joy) packages, with: 
```bash
# On Ubuntu PC
$ roslaunch xbox_teleop xbox_teleop.launch
```

Launch the TurtleBot3 operation packages and enable the robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```


