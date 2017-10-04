# Robot Steering Plugin

Launch the turtlesim with:
```bash
$ 
```

Launch the turtlesim keyboard teleop with:
```bash
$ rosrun turtlesim turtle_teleop_key /turtle1/cmd_vel:=/cmd_vel
```

View the Twist values with:
```bash
$ rostopic echo /cmd_vel
```

Add the [Robot Steering](http://wiki.ros.org/rqt_robot_steering) plugin
in *rqt* under **Plugins-->Robot Tools-->Robot Steering**.