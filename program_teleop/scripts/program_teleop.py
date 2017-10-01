#!/usr/bin/env python

import time

import rospy
from geometry_msgs.msg import Twist


class Robot(object):
    rate = 100
    stop = Twist()
    stop.linear.x = 0
    stop.linear.y = 0
    stop.linear.z = 0
    stop.angular.x = 0
    stop.angular.y = 0
    stop.angular.z = 0

    def __init__(self, pub):
        self.__pub = pub

    def move(self, lin_speed, distance):
        # distance = speed * time

        t = Twist()
        t.linear.x = lin_speed
        t.linear.y = 0
        t.linear.z = 0
        t.angular.x = 0
        t.angular.y = 0
        t.angular.z = 0
        rate = rospy.Rate(Robot.rate)
        start = rospy.get_rostime().to_sec()

        try:
            while True:
                pub.publish(t)
                elapsed = rospy.get_rostime().to_sec() - start
                if elapsed >= distance / abs(lin_speed):
                    break
                rate.sleep()
        finally:
            pub.publish(Robot.stop)

    def rotate(self, ang_speed, degrees):
        # ang_speed units are radians/sec
        # 1 degree = 0.0174533

        t = Twist()
        t.linear.x = 0
        t.linear.y = 0
        t.linear.z = 0
        t.angular.x = 0
        t.angular.y = 0
        t.angular.z = ang_speed
        rate = rospy.Rate(Robot.rate)
        start = rospy.get_rostime().to_sec()

        try:
            while True:
                pub.publish(t)
                elapsed = rospy.get_rostime().to_sec() - start
                if elapsed >= degrees * 0.0174533 * abs(ang_speed):
                    break
                rate.sleep()
        finally:
            pub.publish(Robot.stop)

    def pause(self, sleep_secs):
        time.sleep(sleep_secs)


if __name__ == '__main__':
    rospy.init_node('program_teleop')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    r = Robot(pub)

    for i in range(8):
        print("Going forward")
        r.move(3.0, 3.0)
        print("Going backward")
        r.move(-3.0, 3.0)
        print("Turning 90 degrees")
        r.rotate(-1.0, 90)
