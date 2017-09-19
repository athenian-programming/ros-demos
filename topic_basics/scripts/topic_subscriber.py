#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print(msg.data)


if __name__ == '__main__':
    rospy.init_node('topic_subscriber')
    rospy.Subscriber('counter', Int32, callback)
    print("Listening...")
    rospy.spin()
