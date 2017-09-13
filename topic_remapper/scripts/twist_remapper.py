#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def callback(msg):
    global pub
    if msg.angular.z != 0.0 or msg.linear.x != 0.0:
        print("Remapping linear.x={0} angular.z={1}".format(msg.linear.x, msg.angular.z))
    pub.publish(msg)


rospy.init_node('topic_remapper')

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('cmd_vel_mux/input/teleop', Twist, callback)
print "Listening..."

rospy.spin()
