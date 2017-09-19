## Euclid Teleop Remapper

1) Goto the [Monitor](http://euclid.local/#apps) on the Euclid and enable *teleop*
2) Review the topics in the *rqt* **Topic Monitor**

Run *twist_remapper.py* with: 
```bash
# On Ubunutu
$ roslaunch euclid_teleop twist_remapper.launch
```

Alternatively, specify the remapping in the *~/catkin_ws/src/turtlebot3/turtlebot3_bringup/launch/turtlebot3_core.launch* file:
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

The **remap** tag details are [here](http://wiki.ros.org/roslaunch/XML/remap).
