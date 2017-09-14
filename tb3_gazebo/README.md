# TurtleBot3 Keyboard Control with Gazebo Demo

Demo details are [here](http://turtlebot3.robotis.com/en/latest/simulation.html).

Launch simulated turtlebot in gazebo with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

Launch simulated turtlebot with obstacles in gazebo with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

Launch keyboard control with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Visualize the simulation lidar with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
``` 

Launch automatic navigation with:
```bash
# On Ubuntu PC
# Kill keyboard control process first
$ roslaunch turtlebot3_gazebo turtlebot3_simulation.launch
```

