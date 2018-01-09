#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    rate = rospy.Rate(10)

    for i in range(5):
        t = Twist()
        t.linear.x = .5
        t.linear.y = 0
        t.linear.z = 0
        t.angular.x = 0
        t.angular.y = 0
        t.angular.z = 0

        pub.publish(t)

        rate.sleep()
