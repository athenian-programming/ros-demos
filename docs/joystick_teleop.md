# Joystick Teleop

## Setup

Install the necessary packages with:
````bash
# On Ubunutu PC
$ sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
````

Install a joystick viewer with:
```bash
$ sudo apt-get install jstest-gtk
$ jstest-gtk
$ jstest --normal /dev/input/js1
```


## Usage

Launch a [teleop_twist_joy](http://wiki.ros.org/teleop_twist_joy) node with: 
```bash
# On Ubuntu PC
$ roslaunch teleop_twist_joy teleop.launch joy_dev:=/dev/input/js1 joy_config:=xd3 enable_turbo_button:=1
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
