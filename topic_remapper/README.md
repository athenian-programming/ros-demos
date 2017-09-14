## Topic Remapper Demo

1) Goto the [Scenarios on the Euclid](http://euclid.local/#config/scenarios) and run a scenario 
that has a **Robot Movement Controller** Node
2) Goto the [Monitor on the Euclid](http://euclid.local/#apps) and enable *teleop*
3) Review the topics in the *rqt* **Topic Monitor**

Run *twist_remapper.py* with: 
```bash
$ rosrun topic_remapper twist_remapper.py 
```

or:

```bash
$ roslaunch topic_remapper twist_remapper.launch
```

It would be much better to do the remapping in the *~/catkin_ws/src/turtlebot3/turtlebot3_bringup/launch/turtlebot3_core.launch* file:
```xml
<launch>

  <!-- The remap tag has to come before the affected node tag -->
  <remap from="cmd_vel" to="cmd_vel_mux/input/teleop"/>
  
  <node pkg="rosserial_python" type="serial_node.py" name="turtlebot3_core" output="screen">
    <param name="port" value="/dev/ttyACM0"/>
    <param name="baud" value="115200"/>
  </node>

</launch>
``` 

The remap tag details are [here](http://wiki.ros.org/roslaunch/XML/remap).


## XBox Remapper

Install the necessary packages with:
````bash
# On Ubunutu
$ sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
````

Launch the teleoperation packages for XBOX controller with:
```bash
$ sudo xboxdrv --silent
$ roslaunch teleop_twist_joy teleop.launch
```

Run *xbox_remapper.py* with: 
```bash
$ rosrun topic_remapper xbox_remapper.py 
```

or:

```bash
$ roslaunch topic_remapper xbox_remapper.launch
```
