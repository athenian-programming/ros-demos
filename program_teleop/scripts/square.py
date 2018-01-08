#!/usr/bin/env python

import rospy

from turtle_robot import TurtleRobot
from turtle_sim import TurtleSim

if __name__ == '__main__':
    rospy.init_node('square')

    TurtleSim().start()

    tr = TurtleRobot(1)

    for i in range(4):
        print("Going forward")
        tr.move(2.0, 4.0, True)
        print("Turning 90 degrees")
        tr.turn_rel(.75, 90)
