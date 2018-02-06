#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

LINEAR_ADJ = 0.01
ANG_ADJ = 0.1
STOP_FACTOR = 3


def vels(dir, linear_vel, ang_vel):
    return "%s:\tlinear vel %s\t angular vel %s" % (dir, linear_vel, ang_vel)


def bound(val):
    if val < -1.0:
        return -1.0
    elif val > 1.0:
        return 1.0
    else:
        return val


def callback(msg):
    global pub, target_linear, target_ang, curr_linear, curr_ang

    # Map button cross
    if msg.axes[7] == 1.0:
        target_linear = bound(target_linear + LINEAR_ADJ)
        print(vels("Forward ", target_linear, target_ang))
    elif msg.axes[7] == -1.0:
        target_linear = bound(target_linear - LINEAR_ADJ)
        print(vels("Backward", target_linear, target_ang))
    elif msg.axes[6] == 1.0:
        target_ang = bound(target_ang + ANG_ADJ)
        print(vels("Left    ", target_linear, target_ang))
    elif msg.axes[6] == -1.0:
        target_ang = bound(target_ang - ANG_ADJ)
        print(vels("Right   ", target_linear, target_ang))

    # Map left joystick
    elif msg.axes[1] > 0.0:
        target_linear = bound(target_linear + (LINEAR_ADJ * msg.axes[1]))
        print(vels("Forward   ", target_linear, target_ang))
    elif msg.axes[1] < 0.0:
        target_linear = bound(target_linear - (LINEAR_ADJ * -msg.axes[1]))
        print(vels("Backward   ", target_linear, target_ang))
    elif msg.axes[0] > 0.0:
        target_ang = bound(target_ang + (ANG_ADJ * msg.axes[0]))
        print(vels("Left    ", target_linear, target_ang))
    elif msg.axes[0] < 0.0:
        target_ang = bound(target_ang - (ANG_ADJ * -msg.axes[0]))
        print(vels("Right   ", target_linear, target_ang))

    # Map all right button presses to stop
    elif msg.buttons[0] == 1 or msg.buttons[1] == 1 or msg.buttons[2] == 1 or msg.buttons[3] == 1:
        linear_delta = LINEAR_ADJ * STOP_FACTOR
        if target_linear <= -linear_delta:
            target_linear = target_linear + linear_delta
        elif target_linear >= linear_delta:
            target_linear = target_linear - linear_delta
        else:
            target_linear = 0
            curr_linear = 0

        ang_delta = ANG_ADJ * STOP_FACTOR
        if target_ang <= -ang_delta:
            target_ang = target_ang + ang_delta
        elif target_ang >= ang_delta:
            target_ang = target_ang - ang_delta
        else:
            target_ang = 0
            curr_ang = 0

        print(vels("Stop    ", target_linear, target_ang))

    if target_linear > curr_linear:
        curr_linear = min(target_linear, curr_linear + (LINEAR_ADJ / 4.0))
    else:
        curr_linear = target_linear

    if target_ang > curr_ang:
        curr_ang = min(target_ang, curr_ang + (ANG_ADJ / 4.0))
    else:
        curr_ang = target_ang

    twist = Twist()
    twist.linear.x = bound(curr_linear)
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = bound(curr_ang)
    pub.publish(twist)


def main():
    target_linear = 0
    target_ang = 0
    curr_linear = 0
    curr_ang = 0

    rospy.init_node('xbox_teleop')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
    rospy.Subscriber('/joy', Joy, callback)
    print("Listening...")

    rospy.spin()


if __name__ == '__main__':
    main()
