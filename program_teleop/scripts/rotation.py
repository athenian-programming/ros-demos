#!/usr/bin/env python

import time

import rospy

from turtle_robot import TurtleRobot
from turtle_sim import TurtleSim


def main():
    rospy.init_node('simple_rotation')

    TurtleSim().start()
    tr = TurtleRobot(1)

    print("Turning 360 degrees counter-clockwise")
    for a in range(0, 361, 90):
        tr.turn_abs(1, a)
        time.sleep(1)

    print("Turning 360 degrees clockwise")
    for a in range(0, 361, 90):
        tr.turn_abs(1, -a)
        time.sleep(1)

    print("Done!!")


if __name__ == '__main__':
    main()
