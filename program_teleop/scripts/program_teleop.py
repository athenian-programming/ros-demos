#!/usr/bin/env python

import math
import time

import rospy
# from /opt/ros/kinetic/lib/python2.7/dist-packages/geometry_msgs/msg
from geometry_msgs.msg import Twist
# from /opt/ros/kinetic/lib/python2.7/dist-packages/std_srvs/srv
from std_srvs.srv import Empty
from turtlesim.msg import Pose


class Robot(object):
    rate = 200
    stop = Twist()
    stop.linear.x = 0
    stop.linear.y = 0
    stop.linear.z = 0
    stop.angular.x = 0
    stop.angular.y = 0
    stop.angular.z = 0

    def __init__(self, turtle_num):
        self.__pos_sub = rospy.Subscriber('/turtle' + str(turtle_num) + '/pose', Pose, self.turtle_pose)
        self.__pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
        self.__current_pose = None

    def turtle_pose(self, msg):
        self.__current_pose = msg
        # print("X={0} Y={1} theta={2}".format(self.__current_pose.x, self.__current_pose.y,
        #                                     math.degrees(self.__current_pose.theta)))

    @property
    def curr_theta_degrees(self):
        if self.__current_pose is None:
            return None
        # Pause to get latest update on current pose
        time.sleep(.1)
        return math.degrees(self.__current_pose.theta)

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
        total_time = dist / sp

        try:
            while True:
                if rospy.get_rostime().to_sec() - start >= total_time:
                    break
                self.__pub.publish(t)
                rate.sleep()
        finally:
            self.__pub.publish(Robot.stop)

    def _degrees_diff(self, curr_val, target_val):
        if curr_val <= 180:
            diff = target_val - (curr_val + 360 if target_val > 180 else curr_val)
        else:
            diff = (target_val + 360 if target_val <= 180 else target_val) - curr_val

        if diff < -180:
            return diff + 360
        elif diff > 180:
            return diff - 360
        else:
            return diff

    def _rotate(self, ang_speed, degrees):
        # ang_speed units are radians/sec

        sp = abs(ang_speed)
        t = Twist()
        t.linear.x = 0
        t.linear.y = 0
        t.linear.z = 0
        t.angular.x = 0
        t.angular.y = 0
        t.angular.z = -1 * sp if degrees < 0 else sp

        rate = rospy.Rate(Robot.rate)
        start = rospy.get_rostime().to_sec()
        total_time = math.radians(abs(degrees)) / sp
        try:
            while True:
                if rospy.get_rostime().to_sec() - start >= total_time:
                    break
                self.__pub.publish(t)
                rate.sleep()
        finally:
            self.__pub.publish(Robot.stop)

    def turn_abs(self, ang_speed, abs_degrees):
        if self.curr_theta_degrees is None:
            return
        print("Absolute to {0} degrees".format(abs_degrees))
        diff = self._degrees_diff(self.curr_theta_degrees, abs_degrees)
        print(
            "Current angle: {0}, Absolute target angle: {1}, Diff angle: {2}".format(self.curr_theta_degrees,
                                                                                     abs_degrees,
                                                                                     diff))
        self._rotate(ang_speed, diff)

    def turn_rel(self, ang_speed, rel_degrees):
        if self.curr_theta_degrees is None:
            return
        print("Relative to {0} degrees".format(rel_degrees))
        diff = rel_degrees  # self._degrees_diff(self.curr_theta_degrees, self.curr_theta_degrees + rel_degrees)
        print(
            "Current angle: {0}, Relative target angle: {1}, Diff angle: {2}".format(self.curr_theta_degrees,
                                                                                     rel_degrees,
                                                                                     diff))
        self._rotate(ang_speed, diff)


def pause(self, sleep_secs):
    time.sleep(sleep_secs)


class TurtleSim(object):
    def __init__(self):
        pass

    def reset(self):
        rospy.wait_for_service('reset')
        try:
            reset = rospy.ServiceProxy('reset', Empty)
            reset()
        except rospy.ServiceException as e:
            print("/reset call failed: %s" % e)

    def clear(self):
        rospy.wait_for_service('clear')
        try:
            clear = rospy.ServiceProxy('clear', Empty)
            clear()
        except rospy.ServiceException as e:
            print("/clear call failed: %s" % e)


if __name__ == '__main__':
    rospy.init_node('program_teleop')

    ts = TurtleSim()
    ts.reset()

    r = Robot(1)

    # Pause to give pose subscriber a chance to get data
    time.sleep(.5)

    if False:
        for a in range(0, 450, 90):
            r.turn_abs(1, a)
            time.sleep(1)

        for a in range(0, 450, 90):
            r.turn_abs(1, -a)
            time.sleep(1)

    r.turn_abs(1, 90)

    for a in [0, 60, 120, 180, 240, 300, 360]:
        r.turn_rel(1, a)
        r.turn_rel(1, -a)


    if False:
        for i in range(1):
            print("Going forward")
            r.move(2.0, 4.0, True)
            print("Going backward")
            r.move(1.5, 4.0, 0)
            print("Turning 90 degrees")
            r.turn_rel(.75, 90)

        for d in range(0, 90, 10):
            r.turn_abs(1, d)

        for d in range(360, 0, -10):
            r.turn_abs(1, d)
