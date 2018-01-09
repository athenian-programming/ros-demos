#!/usr/bin/env python

import time

import rospy
from geometry_msgs.msg import Twist

from turtle_robot import TurtleRobot

if __name__ == '__main__':
    rospy.init_node('raw_twist')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    t = Twist()
    t.linear.x = .5
    t.linear.y = 0
    t.linear.z = 0
    t.angular.x = 0
    t.angular.y = 0
    t.angular.z = 0

    pub.publish(t)
    time.sleep(.5)

    pub.publish(TurtleRobot.new_twist(0, 0))
