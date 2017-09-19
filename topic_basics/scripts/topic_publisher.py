#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('topic_publisher')
    pub = rospy.Publisher('counter', Int32, queue_size=10)
    rate = rospy.Rate(2)
    count = 0

    while not rospy.is_shutdown():
        print("Publishing: " + str(count))
        pub.publish(count)
        count += 1
        rate.sleep()
