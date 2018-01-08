#!/usr/bin/env python

import math
import time

import rospy
# from /opt/ros/kinetic/lib/python2.7/dist-packages/geometry_msgs/msg
from geometry_msgs.msg import Twist
# from /opt/ros/kinetic/lib/python2.7/dist-packages/std_srvs/srv
from turtlesim.msg import Pose


class TurtleRobot(object):
    @staticmethod
    def _new_twist(linear_x, angular_z):
        t = Twist()
        t.linear.x = linear_x
        t.linear.y = 0
        t.linear.z = 0
        t.angular.x = 0
        t.angular.y = 0
        t.angular.z = angular_z
        return t

    @staticmethod
    def _distance_diff(curr_x, curr_y, goal_x, goal_y):
        return math.sqrt(math.pow(goal_x - curr_x, 2) + math.pow(goal_y - curr_y, 2))

    def __init__(self, turtle_num):
        self.__rate = 10
        self.__stop = TurtleRobot._new_twist(0, 0)
        self.__current_pose = None

        # Set up subscriber to listen for pose topic messages
        rospy.Subscriber('/turtle' + str(turtle_num) + '/pose', Pose, self._update_pose)

        # Set up publish topic
        self.__pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

        # Pause to give pose subscriber a chance to get data
        time.sleep(.5)

    @property
    def curr_theta_degrees(self):
        # Pause to get latest update on current pose
        time.sleep(.1)
        if self.__current_pose is None:
            print("Warning: current pose not initialized")
            return None
        return math.degrees(self.__current_pose.theta)

    @property
    def curr_xy(self):
        # Pause to get latest update on current pose
        time.sleep(.1)
        if self.__current_pose is None:
            print("Warning: current pose not initialized")
            return None
        return {'x': self.__current_pose.x, 'y': self.__current_pose.y}

    def _update_pose(self, msg):
        self.__current_pose = msg

    def __degrees_diff(self, curr_val, target_val):
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

    def __rotate(self, ang_speed, degrees):
        # ang_speed units are radians/sec
        sp = abs(ang_speed)
        t = TurtleRobot._new_twist(0, -1 * sp if degrees < 0 else sp)

        rate = rospy.Rate(self.__rate)
        start = rospy.get_rostime().to_sec()
        total_time = math.radians(abs(degrees)) / sp
        try:
            while True:
                if rospy.get_rostime().to_sec() - start >= total_time:
                    break
                self.__pub.publish(t)
                rate.sleep()
        finally:
            self.__pub.publish(self.__stop)

    def turn_abs(self, ang_speed, abs_degrees, verbose=False):
        curr = self.curr_theta_degrees
        diff = self.__degrees_diff(curr, abs_degrees)
        if verbose:
            print("Absolute current: {}, Absolute target: {}, Diff: {}".format(curr, abs_degrees, diff))
        self.__rotate(ang_speed, diff)

    def turn_rel(self, ang_speed, rel_degrees, verbose=False):
        if verbose:
            print("Relative current: {}, Relative target: {}".format(self.curr_theta_degrees, rel_degrees))
        self.__rotate(ang_speed, rel_degrees)

    def move(self, lin_speed, distance, isForward):
        # distance = speed * time
        sp = abs(lin_speed)
        dist = abs(distance)
        t = TurtleRobot._new_twist(sp if isForward else -1 * sp, 0)

        rate = rospy.Rate(self.__rate)
        start = rospy.get_rostime().to_sec()
        total_time = dist / sp
        try:
            while True:
                if rospy.get_rostime().to_sec() - start >= total_time:
                    break
                self.__pub.publish(t)
                rate.sleep()
        finally:
            self.__pub.publish(self.__stop)

    def goto(self, goal_x, goal_y, tolerance, verbose=False):
        rate = rospy.Rate(self.__rate)
        try:
            while True:
                curr = self.__current_pose
                linear_diff = TurtleRobot._distance_diff(curr.x, curr.y, goal_x, goal_y)
                ang_diff = math.atan2(goal_y - curr.y, goal_x - curr.x)
                if verbose:
                    print("Dist: {} Angle: {} Curr: {},{}".format(linear_diff, ang_diff - curr.theta, curr.x, curr.y))
                if linear_diff < tolerance:
                    break
                self.__pub.publish(TurtleRobot._new_twist(.4 * linear_diff, 1.75 * (ang_diff - curr.theta)))
                rate.sleep()
        finally:
            self.__pub.publish(self.__stop)
