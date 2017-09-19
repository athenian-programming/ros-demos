#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


def vels(dir, target_linear_vel, target_ang_vel):
    return "%s:\tlinear vel %s\t angular vel %s" % (dir, target_linear_vel, target_ang_vel)


def linear_callback(msg):
    global linear_init, target_linear_vel, control_linear_vel, target_ang_vel

    raw_val = max(-1.0, min(1.0, int((msg.pose.pose.orientation.y * 10)) / 5.0))

    if linear_init is None:
        linear_init = raw_val

    # Normalize to initial value
    val = raw_val - linear_init

    if val >= 0.1:
        target_linear_vel = val
        control_linear_vel = min(1.0,
                                 control_linear_vel + (
                                     0.01 * val)) if target_linear_vel > control_linear_vel else target_linear_vel
        print(vels("Forward   ", target_linear_vel, target_ang_vel))
    elif val <= -0.1:
        target_linear_vel = val
        control_linear_vel = max(-1.0,
                                 control_linear_vel - (
                                     0.01 * -val)) if target_linear_vel < control_linear_vel else target_linear_vel
        print(vels("Backward   ", target_linear_vel, target_ang_vel))
    else:
        target_linear_vel = 0
        control_linear_vel = 0
        print(vels("Linear Stop", target_linear_vel, target_ang_vel))


def ang_callback(msg):
    global ang_init, target_ang_vel, control_ang_vel, target_linear_vel

    raw_val = max(-1.0, min(1.0, int((msg.pose.pose.orientation.z * 10)) / 5.0))

    if ang_init is None:
        ang_init = raw_val

    # Normalize to initial value
    val = raw_val - ang_init

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
    linear_init = None
    ang_init = None
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
        print("Writing: " + control_linear_vel)
        pub.publish(twist)
        rate.sleep()
