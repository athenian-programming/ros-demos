#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

def callback(msg):
    # global pub
    if msg.axes[6] != 0.0 or msg.axes[7] != 0.0:
        print("Remapping {0} {1}".format(msg.axes[6], msg.axes[7]))
        # pub.publish(msg)


rospy.init_node('xbox_remapper')

# pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('joy/axes', Joy, callback)
print "Listening..."

rospy.spin()
