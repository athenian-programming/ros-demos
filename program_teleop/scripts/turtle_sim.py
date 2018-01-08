#!/usr/bin/env python

import rospy
# from /opt/ros/kinetic/lib/python2.7/dist-packages/geometry_msgs/msg
from std_srvs.srv import Empty


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

    def start(self):
        self.reset()
        self.clear()
