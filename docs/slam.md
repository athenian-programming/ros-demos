# SLAM Notes


Launch either a simulated or real TurtleBot3 with: 

```bash
# On Ubuntu PC
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
# or
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

Launch keyboard teleop control with: 
```bash
# On Ubuntu PC
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Launch the SLAM file with: 
```bash
$ roslaunch turtlebot3_slam turtlebot3_slam.launch
```

Visualize the model in 3D with RViz with:
```bash
$ rosrun rviz rviz -d `rospack find turtlebot3_slam`/rviz/turtlebot3_slam.rviz
```

Save the map with:
```bash
$ rosrun map_server map_saver -f ~/map
```