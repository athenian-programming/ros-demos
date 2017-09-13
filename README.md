# ROS Demos

### TurtleBot3 Demo

Demo details are [here](http://turtlebot3.robotis.com/en/latest/bringup.html).

Launch turtlebot3 operation packages and enable robot with:
```bash
# On TurtleBot3
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Launch keyboard control with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Examine the topics and values with either *rqt* or *rqt_plot*.
With *rqt* add the following plugins:
   1) **Plugins-->Topics-->TopicMonitor** 
   2) **Plugins-->Visualization-->Plot**. 


Plot these topics:
 1) **/cmd_vel/linear/x** for keystroke control.
 2) **/imu/orientation/z** for robot rotation.


Launch RViz viewer with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_bringup turtlebot3_model.launch
```

### TurtleBot3 Gazebo Demo

Demo details are [here](http://turtlebot3.robotis.com/en/latest/simulation.html).

Launch keyboard control with: 
```bash
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Launch simulated turtlebot in gazebo with: 
```bash
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

Launch simulated turtlebot with obstacles in gazebo with: 
```bash
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

Visualize the simulation lidar with: 
```bash
$ roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
``` 

Launch automatic navigation with:
```bash
# Kill keyboard controll process first
$ roslaunch turtlebot3_gazebo turtlebot3_simulation.launch
```


