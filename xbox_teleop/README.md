# XBox Teleop

## Usage

Launch the TurtleBot3 operation packages and enable the robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Launch the Xbox USB Gamepad Userspace Driver with:
```bash
$ sudo xboxdrv --silent
# If you get a LIBUSB_ERROR_BUSY error, resolve it with:
# sudo rmmod xpad
```

Run *xbox_remapper.launch* with: 
```bash
On Ubuntu PC
$ roslaunch topic_remapper xbox_teleop.launch
```

This launches both the xbox_teleop node and the teleoperation package for the XBox controller.


## Setup

Install the necessary packages with:
````bash
# On Ubunutu PC
$ sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
````
