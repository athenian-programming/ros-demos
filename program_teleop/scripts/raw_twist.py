#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

from turtle_robot import TurtleRobot


def main():
    # This is required
    rospy.init_node('raw_twist')

    # Setup publisher with topic name, message type and queue size
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    # Create a Twist message
    t = Twist()
    t.linear.x = 1
    t.linear.y = 0
    t.linear.z = 0
    t.angular.x = 0
    t.angular.y = 0
    t.angular.z = 0

    for i in range(30):
        pub.publish(t)  # Publish the twist message
        rospy.sleep(.1)  # Give the robot a chance to move

    for i in range(30):
        pub.publish(TurtleRobot.new_twist(-1, 0))  # Publish the twist message
        rospy.sleep(.1)  # Give the robot a chance to move

    # Stop the robot
    pub.publish(TurtleRobot.new_twist(0, 0))
    rospy.sleep(1.0)


if __name__ == '__main__':
    main()
