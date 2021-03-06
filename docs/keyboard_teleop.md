# Keyboard Teleop

Demo details are [here](http://turtlebot3.robotis.com/en/latest/bringup.html).

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
 
Launch a TurtleBot3 with:
```bash
# On TurtleBot3
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Launch a simulated turtle robot with:
```bash
# On Ubuntu PC
rosrun turtlesim turtlesim_node /turtle1/cmd_vel:=/cmd_vel
```

Launch a TurtleBot3 in Gazebo with:
```bash
# On Ubuntu PC
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```



