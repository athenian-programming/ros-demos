#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

INC = 0.01 / 4.0


def vels(dir, target, control):
    return "%s:\tcontrol vel %s\t target vel %s" % (dir, target, control)


def linear_callback(msg):
    global linear_adj, target_linear_vel, control_linear_vel, target_ang_vel

    raw_val = max(-1.0, min(1.0, int((msg.pose.pose.orientation.y * 10)) / 5.0))

    if linear_adj is None:
        linear_adj = raw_val

    # Normalize to initial value
    val = raw_val - linear_adj

    if val >= 0.1:
        target_linear_vel = val
        if target_linear_vel > control_linear_vel:
            control_linear_vel = control_linear_vel + INC
        elif target_linear_vel < control_linear_vel:
            control_linear_vel = control_linear_vel - INC
        else:
            control_linear_vel = target_linear_vel
        control_linear_vel = min(1.0, control_linear_vel)
        print(vels("Forward   ", control_linear_vel, target_linear_vel))
    elif val <= -0.1:
        target_linear_vel = val
        if target_linear_vel > control_linear_vel:
            control_linear_vel = control_linear_vel - INC
        elif target_linear_vel < control_linear_vel:
            control_linear_vel = control_linear_vel + INC
        else:
            control_linear_vel = target_linear_vel
        control_linear_vel = max(-1.0, control_linear_vel)
        print(vels("Backward   ", control_linear_vel, target_linear_vel))
    else:
        target_linear_vel = 0
        if control_linear_vel >= 0.1:
            control_linear_vel = control_linear_vel - INC
        elif control_linear_vel <= -0.1:
            control_linear_vel = control_linear_vel + INC
        else:
            control_linear_vel = 0
        print(vels("Linear Stop", control_linear_vel, target_linear_vel))


def ang_callback(msg):
    global ang_adj, target_ang_vel, control_ang_vel, target_linear_vel

    raw_val = max(-1.0, min(1.0, int((msg.pose.pose.orientation.z * 10)) / 5.0))

    if ang_adj is None:
        ang_adj = raw_val

    # Normalize to initial value
    val = raw_val - ang_adj

    if val >= 0.1:
        target_ang_vel = target_ang_vel + (0.01 * val)
        print(vels("Left    ", target_linear_vel, target_ang_vel))
    elif val <= -0.1:
        target_ang_vel = target_ang_vel - (0.01 * -val)
        print(vels("Right   ", target_linear_vel, target_ang_vel))
    else:
        target_ang_vel = 0
        control_ang_vel = 0
        print(vels("Angular Stop", target_linear_vel, target_ang_vel))

    control_ang_vel = min(target_ang_vel,
                          control_ang_vel + (0.01 / 4.0)) if target_ang_vel > control_ang_vel else target_ang_vel


if __name__ == '__main__':
    linear_adj = None
    ang_adj = None
    target_linear_vel = 0
    target_ang_vel = 0
    control_linear_vel = 0
    control_ang_vel = 0

    rospy.init_node('imu_teleop')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
    rospy.Subscriber('/realsense/odom', Odometry, linear_callback)  # /pose/pose/orientation/y
    #rospy.Subscriber('/realsense/odom', Odometry, ang_callback)  # /pose/pose/orientation/z

    print("Listening...")

    rate = rospy.Rate(10)

    while True:
        twist = Twist()
        twist.linear.x = control_linear_vel
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = control_ang_vel
        pub.publish(twist)
        rate.sleep()
