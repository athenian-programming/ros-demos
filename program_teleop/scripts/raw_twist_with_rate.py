#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

from turtle_robot import TurtleRobot

if __name__ == '__main__':

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    rate = rospy.Rate(10)

    for i in range(5):
        pub.publish(TurtleRobot.new_twist(0, .5))
        rate.sleep()

    pub.publish(TurtleRobot.new_twist(0, 0))
