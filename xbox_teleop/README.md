# XBox Teleop

## Description

The *xbox_teleop.py* program subscribes to */joy* and publishes Twist values to */cmd_vel*.

## Setup

Install the necessary packages with:
````bash
# On Ubunutu PC
sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
````

Install a joystick viewer with:
```bash
sudo apt-get install jstest-gtk
jstest-gtk
jstest --normal /dev/input/js1
```

## Usage

Launch the Xbox USB Gamepad Userspace Driver with:
```bash
sudo xboxdrv --silent
# If you get a LIBUSB_ERROR_BUSY error, resolve it with:
# sudo rmmod xpad
# To deal with this automatically, manually edit https://andrewdai.co/xbox-controller-ros.html and add
# "blacklist xpad"  See https://andrewdai.co/xbox-controller-ros.html
```

Run *xbox_remapper.launch*, which launches both the xbox_teleop node and 
the [teleop_twist_joy](http://wiki.ros.org/teleop_twist_joy) packages, with: 
```bash
# On Ubuntu PC
roslaunch xbox_teleop xbox_teleop.launch
```

Alternatively, you can use a ROS package to do the remapping.  
Launch a [teleop_twist_joy](http://wiki.ros.org/teleop_twist_joy) node with: 
```bash
# On Ubuntu PC
roslaunch teleop_twist_joy teleop.launch joy_dev:=/dev/input/js0 joy_config:=xbox enable_turbo_button:=1
```

Values will not be published to **/cmd_vel** unless a deadman button (**X**) is pressed. 
The upper right trigger button is a turbo deadman button.


Launch a robot with:
```bash
# On TurtleBot3
roslaunch turtlebot3_bringup turtlebot3_robot.launch

# On Ubuntu PC
rosrun turtlesim turtlesim_node /turtle1/cmd_vel:=/cmd_vel

# On Ubuntu PC
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```