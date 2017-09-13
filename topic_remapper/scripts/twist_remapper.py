#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def callback(msg):
    global pub
    print "Remapping value"
    pub.publish(msg)
    

rospy.init_node('twist-remapper')

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('cmd_vel_mux/input/teleop', Twist, callback)
print "Listening..."

rospy.spin()
