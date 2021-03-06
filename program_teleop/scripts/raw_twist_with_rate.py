#!/usr/bin/env python

import time

import rospy
from geometry_msgs.msg import Twist

from turtle_robot import TurtleRobot


def main():
    rospy.init_node('raw_twist_with_rate')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    rate = rospy.Rate(10)

    print("Rotate")
    for i in range(50):
        pub.publish(TurtleRobot.new_twist(0, 1))
        rate.sleep()

    time.sleep(2)

    print("Go straight")
    for i in range(10):
        pub.publish(TurtleRobot.new_twist(1, 0))
        rate.sleep()

    time.sleep(2)

    print("Rotate and go straight")
    for i in range(50):
        pub.publish(TurtleRobot.new_twist(1, 1))
        rate.sleep()

    pub.publish(TurtleRobot.new_twist(0, 0))


if __name__ == '__main__':
    main()
