# Keyboard Control with Gazebo 

A complete description is [here](http://turtlebot3.robotis.com/en/latest/simulation.html).

Launch simulated TurtleBot3 in [Gazebo](http://gazebosim.org) with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

Launch simulated TurtleBot3 with obstacles in Gazebo with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

Launch keyboard teleop control with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Visualize the lidar simulation with: 
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

