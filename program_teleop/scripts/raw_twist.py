#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

from turtle_robot import TurtleRobot

if __name__ == '__main__':
    # This is required
    rospy.init_node('raw_twist')

    # Setup publisher
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    # Create a Twist message
    t = Twist()
    t.linear.x = 1
    t.linear.y = 0
    t.linear.z = 0
    t.angular.x = 0
    t.angular.y = 0
    t.angular.z = 0

    # Publish the twist message
    pub.publish(t)

    # Give the robot a chance to move
    rospy.sleep(2.0)

    # Stop the robot
    pub.publish(TurtleRobot.new_twist(0, 0))
    rospy.sleep(2.0)
