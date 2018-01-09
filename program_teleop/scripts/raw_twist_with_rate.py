#!/usr/bin/env python

import time

import rospy
from geometry_msgs.msg import Twist

from turtle_robot import TurtleRobot

if __name__ == '__main__':
    rospy.init_node('raw_twist_with_rate')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    rate = rospy.Rate(10)

    print("Rotating")
    for i in range(50):
        pub.publish(TurtleRobot.new_twist(0, 1))
        rate.sleep()

    time.sleep(2)

    print("Going straight")
    for i in range(10):
        pub.publish(TurtleRobot.new_twist(1, 0))
        rate.sleep()

    time.sleep(2)

    print("Rotating and going straight")
    for i in range(50):
        pub.publish(TurtleRobot.new_twist(1, 1))
        rate.sleep()

    pub.publish(TurtleRobot.new_twist(0, 0))
