#!/usr/bin/env python

import time

import rospy

from turtle_robot import TurtleRobot
from turtle_sim import TurtleSim

if __name__ == '__main__':
    rospy.init_node('program_teleop')

    ts = TurtleSim()
    ts.reset()

    tr = TurtleRobot(1)

    # Pause to give pose subscriber a chance to get data
    time.sleep(.5)

    curr = tr.curr_xy
    print("Current x,y: {0},{1}".format(curr['x'], curr['y']))
    tr.goto(2, 2, .25)
    tr.goto(2, 9, .25)
    tr.goto(9, 9, .25)
    tr.goto(9, 2, .25)

    if False:
        for a in range(0, 450, 90):
            tr.turn_abs(1, a)
            time.sleep(1)

        for a in range(0, 450, 90):
            tr.turn_abs(1, -a)
            time.sleep(1)

    if False:
        tr.turn_abs(1, 90)

        for a in [0, 60, 120, 180, 240, 300, 360]:
            tr.turn_rel(1, a)
            tr.turn_rel(1, -a)

    if False:
        for i in range(1):
            print("Going forward")
            tr.move(2.0, 4.0, True)
            print("Going backward")
            tr.move(1.5, 4.0, 0)
            print("Turning 90 degrees")
            tr.turn_rel(.75, 90)

        for d in range(0, 90, 10):
            tr.turn_abs(1, d)

        for d in range(360, 0, -10):
            tr.turn_abs(1, d)
