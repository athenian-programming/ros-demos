#!/usr/bin/env python

import time

import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('latched_topic_publisher')
    pub = rospy.Publisher('counter', Int32, latch=True, queue_size=10)
    count = 0

    while not rospy.is_shutdown():
        print "Publishing latched: " + str(count)
        pub.publish(count)
        count += 1
        time.sleep(60)
