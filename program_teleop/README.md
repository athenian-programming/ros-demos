# Programatic Teleop

The [ros_tutorials](https://github.com/ros/ros_tutorials) package includes a [turtle simulator](http://wiki.ros.org/turtlesim). You control
the turtle with [Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html) messages, just like any other physical or virtual robot in ROS.


Launch the turtle simulator with:
```bash
rosrun turtlesim turtlesim_node /turtle1/cmd_vel:=/cmd_vel
```

Move the turtle with:
```bash
rosrun program_teleop raw_twist.py
rosrun program_teleop raw_twist_with_rate.py
rosrun program_teleop rotation.py
rosrun program_teleop square.py
rosrun program_teleop multi_goto.py
```
