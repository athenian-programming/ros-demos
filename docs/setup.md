# Admin Notes

## Adding packages

Create **new_package_name**, which depends on **std_msgs** and **rospy**, with:
```bash
$ cd ~/catkin_ws/ros_demos/src/ros_demos
$ catkin_create_pkg new_package_name std_msgs rospy
```

## Adjusting the PyCharm Interpreter Path

Add */opt/ros/kinetic/lib/python2.7/dist-packages* to the 
interpreter path with:

1) Open the Preferences panel 

2) Double click on `Project:your-project-name`

3) Select the `Project Interpreter`  

4) Click on icon to the right of the "Project Interpreter" value

5) Click on `More...`
 
6) Select the interpreter you are using 

7) Click on the tree symbol 
<img title="Show paths for the selected interpreter" src="https://www.jetbrains.com/help/img/idea/2016.3/icon_show_paths.png" width="21" height="19">
at the bottom of the dialog (hovering over the symbol reveals "Show paths for the selected interpreter")

8) Click on the "plus" symbol 
<img title="Add ⌘N" src="https://www.jetbrains.com/help/img/idea/2016.3/new.png" width="12" height="12">
and add */opt/ros/kinetic/lib/python2.7/dist-packages*.
