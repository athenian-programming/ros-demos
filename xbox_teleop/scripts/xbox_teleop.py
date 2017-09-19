#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

LINEAR_ADJ = 0.01
ANG_ADJ = 0.1
STOP_FACTOR = 3


def vels(dir, target_linear_vel, target_ang_vel):
    return "%s:\tlinear vel %s\t angular vel %s" % (dir, target_linear_vel, target_ang_vel)


def bound(val):
    if val < -1.0:
        return -1.0
    elif val > 1.0:
        return 1.0
    else:
        return val


def callback(msg):
    global pub, target_linear_vel, target_ang_vel, control_linear_vel, control_ang_vel

    # Map button cross
    if msg.axes[7] == 1.0:
        target_linear_vel = bound(target_linear_vel + LINEAR_ADJ)
        print(vels("Forward ", target_linear_vel, target_ang_vel))
    elif msg.axes[7] == -1.0:
        target_linear_vel = bound(target_linear_vel - LINEAR_ADJ)
        print(vels("Backward", target_linear_vel, target_ang_vel))
    elif msg.axes[6] == 1.0:
        target_ang_vel = bound(target_ang_vel + ANG_ADJ)
        print(vels("Left    ", target_linear_vel, target_ang_vel))
    elif msg.axes[6] == -1.0:
        target_ang_vel = bound(target_ang_vel - ANG_ADJ)
        print(vels("Right   ", target_linear_vel, target_ang_vel))

    # Map left joystick
    elif msg.axes[1] > 0.0:
        target_linear_vel = bound(target_linear_vel + (LINEAR_ADJ * msg.axes[1]))
        print(vels("Forward   ", target_linear_vel, target_ang_vel))
    elif msg.axes[1] < 0.0:
        target_linear_vel = bound(target_linear_vel - (LINEAR_ADJ * -msg.axes[1]))
        print(vels("Backward   ", target_linear_vel, target_ang_vel))
    elif msg.axes[0] > 0.0:
        target_ang_vel = bound(target_ang_vel + (ANG_ADJ * msg.axes[0]))
        print(vels("Left    ", target_linear_vel, target_ang_vel))
    elif msg.axes[0] < 0.0:
        target_ang_vel = bound(target_ang_vel - (ANG_ADJ * -msg.axes[0]))
        print(vels("Right   ", target_linear_vel, target_ang_vel))

    # Map all right button presses to stop
    elif msg.buttons[0] == 1 or msg.buttons[1] == 1 or msg.buttons[2] == 1 or msg.buttons[3] == 1:
        linear_delta = LINEAR_ADJ * STOP_FACTOR
        if target_linear_vel <= -linear_delta:
            target_linear_vel = target_linear_vel + linear_delta
        elif target_linear_vel >= linear_delta:
            target_linear_vel = target_linear_vel - linear_delta
        else:
            target_linear_vel = 0
            control_linear_vel = 0

        ang_delta = ANG_ADJ * STOP_FACTOR
        if target_ang_vel <= -ang_delta:
            target_ang_vel = target_ang_vel + ang_delta
        elif target_ang_vel >= ang_delta:
            target_ang_vel = target_ang_vel - ang_delta
        else:
            target_ang_vel = 0
            control_ang_vel = 0

        print(vels("Stop    ", target_linear_vel, target_ang_vel))

    if target_linear_vel > control_linear_vel:
        control_linear_vel = min(target_linear_vel, control_linear_vel + (LINEAR_ADJ / 4.0))
    else:
        control_linear_vel = target_linear_vel

    if target_ang_vel > control_ang_vel:
        control_ang_vel = min(target_ang_vel, control_ang_vel + (ANG_ADJ / 4.0))
    else:
        control_ang_vel = target_ang_vel

    twist = Twist()
    twist.linear.x = bound(control_linear_vel)
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = bound(control_ang_vel)
    pub.publish(twist)


if __name__ == '__main__':
    target_linear_vel = 0
    target_ang_vel = 0
    control_linear_vel = 0
    control_ang_vel = 0

    rospy.init_node('xbox_remapper')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
    sub = rospy.Subscriber('/joy', Joy, callback)
    print("Listening...")

    rospy.spin()
