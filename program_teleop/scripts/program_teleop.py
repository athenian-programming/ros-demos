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

    def move(self, lin_speed, distance, isForward):
        # distance = speed * time

        sp = abs(lin_speed)
        dist = abs(distance)
        t = Twist()
        t.linear.x = sp if isForward else -1 * sp
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
                if elapsed >= dist / sp:
                    break
                rate.sleep()
        finally:
            pub.publish(Robot.stop)

    def rotate(self, ang_speed, degrees, clockwise):
        # ang_speed units are radians/sec
        # 1 degree = 0.0174533

        sp = abs(ang_speed)
        radians = abs(degrees) * 0.0174533
        t = Twist()
        t.linear.x = 0
        t.linear.y = 0
        t.linear.z = 0
        t.angular.x = 0
        t.angular.y = 0
        t.angular.z = -1 * sp if clockwise else sp
        rate = rospy.Rate(Robot.rate)
        start = rospy.get_rostime().to_sec()

        try:
            while True:
                pub.publish(t)
                elapsed = rospy.get_rostime().to_sec() - start
                if elapsed >= radians * sp:
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
        r.move(3.0, 3.0, True)
        print("Going backward")
        r.move(-3.0, 3.0, 0)
        print("Turning 90 degrees")
        r.rotate(-1.0, 90, 1)
        print("Turning 180 degrees")
        r.rotate(-1.0, 180, False)
