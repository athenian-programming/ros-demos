# ROS Demos

## Demos

* [Topic Basics](topic_basics/)
* [Keyboard Teleop](docs/keyboard_teleop.md)
* [Robot Steering rqt plugin](docs/robot_steering.md)
* [XBox Teleop](xbox_teleop/)
* [Joystick Teleop](docs/joystick_teleop.md)
* [Euclid Teleop](euclid_teleop/)
* [IMU Teleop](imu_teleop/)
* [Programatic Teleop](program_teleop/)
* [RViz Viewer](docs/rviz.md)
* [TurtleBot3 with Gazebo](docs/gazebo_demo.md)
* [SLAM](docs/slam.md)


## Setup

Add these statements (replacing ubuntu1 with your Ubuntu PC hostname and ubuntu2 with
the hostname of the machine running *roscore*) to your *~/.bashrc*:

```bash
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash

export TURTLEBOT3_MODEL=burger
export ROS_HOSTNAME=ubuntu1
export ROS_MASTER_URI=http://ubuntu2:11311
```

Source *~/.bashrc* to add *catkin_make* to your **PATH**:
```bash
source ~/.bashrc
```

Note: Ignore the **-su: ~/catkin_ws/devel/setup.bash: No such file or directory** message.
Running *catkin_make* in the next step will create the */devel* directory.

Install the *ros-demos* package in *~/catkin/src* with:

```bash
cd ~/catkin_ws/src
git clone https://github.com/athenian-robotics/ros-demos.git
```

Install the TurtleBot3 packages in *~/catkin/src* with:

```bash
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
```

Build the enviroment with:
```bash
cd ~/catkin_ws
catkin_make
```

Source *~/.bashrc* again to verify that everything was built:
```bash
source ~/.bashrc
```

Run *roscore* on your Ubuntu PC with:
```bash
roscore
```

## Adjusting the PyCharm Interpreter Path

Add */opt/ros/kinetic/lib/python2.7/dist-packages* to the 
interpreter path with:

1) Open the Preferences panel 

2) Double click on `Project:your-project-name`

3) Select the `Project Interpreter`  

4) Click on icon to the right of the "Project Interpreter" value

5) Click on `More...`
 
6) Select the interpreter you are using 

7) Click on the tree symbol 
<img title="Show paths for the selected interpreter" src="https://www.jetbrains.com/help/img/idea/2016.3/icon_show_paths.png" width="21" height="19">
at the bottom of the dialog (hovering over the symbol reveals "Show paths for the selected interpreter")

8) Click on the "plus" symbol 
<img title="Add ⌘N" src="https://www.jetbrains.com/help/img/idea/2016.3/new.png" width="12" height="12">
and add */opt/ros/kinetic/lib/python2.7/dist-packages*.

