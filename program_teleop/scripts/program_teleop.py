#!/usr/bin/env python

import time

import rospy
from geometry_msgs.msg import Twist


class Robot(object):
    def __init__(self, pub):
        self.__pub = pub

    def move(self, speed, distance):
        # distance = speed * time

        t1 = Twist()
        t1.linear.x = speed
        t1.linear.y = 0
        t1.linear.z = 0
        t1.angular.x = 0
        t1.angular.y = 0
        t1.angular.z = 0
        rate = rospy.Rate(10)
        start = rospy.get_rostime().secs

        try:
            while True:
                pub.publish(t1)
                elapsed = rospy.get_rostime().secs - start
                if elapsed >= distance / speed:
                    break
                rate.sleep()
        finally:
            t2 = Twist()
            t2.linear.x = 0
            t2.linear.y = 0
            t2.linear.z = 0
            t2.angular.x = 0
            t2.angular.y = 0
            t2.angular.z = 0


if __name__ == '__main__':
    target_linear = 0
    target_ang = 0
    curr_linear = 0
    curr_ang = 0

    rospy.init_node('program_teleop')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    r = Robot(pub)

    r.move(3, 10)
    time.sleep(5)
    r.move(3, -10)
