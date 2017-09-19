# TurtleBot3 Keyboard Teleop Demo

Demo details are [here](http://turtlebot3.robotis.com/en/latest/bringup.html).

Launch the TurtleBot3 operation packages and enable the robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Launch keyboard control with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Launch RViz viewer with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_bringup turtlebot3_model.launch
```

Examine the topics and values with either *rqt* or *rqt_plot*.
With *rqt* add the following plugins:
   1) **Plugins-->Topics-->TopicMonitor** 
   2) **Plugins-->Visualization-->Plot**. 


Plot these topics:
 1) **/cmd_vel/linear/x** for keystroke control.
 2) **/imu/orientation/z** for robot rotation.


