#!/usr/bin/env python

import rospy

from turtle_robot import TurtleRobot
from turtle_sim import TurtleSim

if __name__ == '__main__':
    rospy.init_node('multi_goto')

    TurtleSim().start()

    tr = TurtleRobot(1)

    curr = tr.curr_xy
    print("Current x,y: {0},{1}".format(curr['x'], curr['y']))

    print("Going to 2, 2")
    tr.goto(2, 2, .25)

    print("Going to 2, 9")
    tr.goto(2, 9, .25)

    print("Going to 9, 9")
    tr.goto(9, 9, .25)

    print("Going to 9, 2")
    tr.goto(9, 2, .25)

    print("Going to 5.5, 5.5")
    tr.goto(5.5, 5.5, .25)
