#!/usr/bin/env python

import time

import rospy

from turtle_robot import TurtleRobot
from turtle_sim import TurtleSim

if __name__ == '__main__':
    rospy.init_node('program_teleop')

    ts = TurtleSim()
    ts.reset()
    ts.clear()

    tr = TurtleRobot(1)

    # Pause to give pose subscriber a chance to get data
    time.sleep(.5)

    curr = tr.curr_xy
    print("Current x,y: {0},{1}".format(curr['x'], curr['y']))
    tr.goto(2, 2, .25)
    tr.goto(2, 9, .25)
    tr.goto(9, 9, .25)
    tr.goto(9, 2, .25)
