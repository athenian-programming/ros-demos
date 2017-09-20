#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

INC = 0.01
MULT = 0.25
ZERO_TOP = 0.05
ZERO_BOTTOM = -0.05


def vels(dir, target, control):
    return "%s:\tcontrol vel %s\t target vel %s" % (dir, target, control)


def linear_callback(msg):
    global linear_raw, linear_adj, target_linear, curr_linear

    # linear_raw = max(-1.0, min(1.0, int((msg.pose.pose.orientation.y * 10)) / 5.0))
    linear_raw = max(-1.0, min(1.0, (msg.pose.pose.orientation.y * 10) / 5.0))

    if linear_adj is None:
        linear_adj = linear_raw

    # Normalize to initial value
    target_linear = linear_raw - linear_adj

    if target_linear >= ZERO_TOP:
        if target_linear > curr_linear:
            curr_linear = curr_linear + (INC * MULT)
        elif target_linear < curr_linear:
            curr_linear = curr_linear - (INC * MULT)
        else:
            curr_linear = target_linear
        curr_linear = min(1.0, curr_linear)
        # print(vels("Forward   ", curr_linear, target_linear))
    elif target_linear <= ZERO_BOTTOM:
        if target_linear > curr_linear:
            curr_linear = curr_linear + (INC * MULT)
        elif target_linear < curr_linear:
            curr_linear = curr_linear - (INC * MULT)
        else:
            curr_linear = target_linear
        curr_linear = max(-1.0, curr_linear)
        # print(vels("Backward   ", curr_linear, target_linear))
    else:
        target_linear = 0
        if curr_linear >= ZERO_TOP:
            curr_linear = curr_linear - INC
        elif curr_linear <= ZERO_BOTTOM:
            curr_linear = curr_linear + INC
        else:
            curr_linear = 0
            # print(vels("Linear Stop", curr_linear, target_linear))

    curr_linear = linear_raw - linear_adj

def ang_callback(msg):
    global ang_raw, ang_adj, target_ang, curr_ang

    ang_raw = max(-1.0, min(1.0, int((msg.pose.pose.orientation.z * 10)) / 5.0))

    if ang_adj is None:
        ang_adj = ang_raw

    # Normalize to initial value
    target_ang = ang_raw - ang_adj

    if target_ang >= ZERO_TOP:
        if target_ang > curr_ang:
            curr_ang = curr_ang + (INC * MULT)
        elif target_ang < curr_ang:
            curr_ang = curr_ang - (INC * MULT)
        else:
            curr_ang = target_ang
        curr_ang = min(1.0, curr_ang)
        # print(vels("Right   ", curr_ang, target_ang))
    elif target_ang <= ZERO_BOTTOM:
        if target_ang > curr_ang:
            curr_ang = curr_ang + (INC * MULT)
        elif target_ang < curr_ang:
            curr_ang = curr_ang - (INC * MULT)
        else:
            curr_ang = target_ang
        curr_ang = max(-1.0, curr_ang)
        # print(vels("Left   ", curr_ang, target_ang))
    else:
        target_ang = 0
        if curr_ang >= ZERO_TOP:
            curr_ang = curr_ang - INC
        elif curr_ang <= ZERO_BOTTOM:
            curr_ang = curr_ang + INC
        else:
            curr_ang = 0

            # print(vels("Angular Stop", curr_ang, target_ang))

if __name__ == '__main__':
    linear_raw = 0
    ang_raw = 0
    linear_adj = None
    ang_adj = None
    target_linear = 0
    target_ang = 0
    curr_linear = 0
    curr_ang = 0

    rospy.init_node('imu_teleop')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
    rospy.Subscriber('/realsense/odom', Odometry, linear_callback)  # /pose/pose/orientation/y
    rospy.Subscriber('/realsense/odom', Odometry, ang_callback)  # /pose/pose/orientation/z

    print("Listening...")

    rate = rospy.Rate(10)

    while True:
        twist = Twist()
        twist.linear.x = curr_linear
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = curr_ang
        pub.publish(twist)
        print("linear: %s\tangular: %s" % (linear_raw, ang_raw))
        rate.sleep()
