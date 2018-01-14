# Keyboard Teleop

Demo details are [here](http://turtlebot3.robotis.com/en/latest/bringup.html).

Install these repos in *~/catkin/src*:

```bash
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
cd ~/catkin_ws && catkin_make
```


Launch keyboard control with: 
```bash
# On Ubuntu PC
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Examine the topics and values with either *rqt* or *rqt_plot*.
With *rqt* add the following plugins:
1) **Plugins-->Topics-->TopicMonitor** 
2) **Plugins-->Visualization-->Plot**. 


Plot these topics:
1) **/cmd_vel/linear/x** for keystroke control.
2) **/imu/orientation/z** for robot rotation.
 
 Launch a robot with:
```bash
# On TurtleBot3
roslaunch turtlebot3_bringup turtlebot3_robot.launch

# TurltleSim on Ubuntu PC
rosrun turtlesim turtlesim_node /turtle1/cmd_vel:=/cmd_vel

# Gazebo on Ubuntu PC
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```



