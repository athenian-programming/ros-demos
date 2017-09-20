#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

LINEAR_SENSITIVITY = 3.0
ANG_SENSITIVITY = 3.0

def linear_callback(msg):
    global linear_adj, curr_linear

    # Divide by LINEAR_SENSITIVITY to decrease sensitivity
    linear_raw = max(-1.0, min(1.0, ((msg.pose.pose.orientation.y / LINEAR_SENSITIVITY) * 10) / 5.0))

    if linear_adj is None:
        linear_adj = linear_raw

    # Normalize to initial value
    curr_linear = int((linear_raw - linear_adj) * 100) / 100.0


def ang_callback(msg):
    global ang_adj, curr_ang

    # Multiply by ANG_SENSITIVITY to increase sensitivity
    ang_raw = max(-1.0, min(1.0, (msg.pose.pose.orientation.z * ANG_SENSITIVITY * 10) / 5.0))

    if ang_adj is None:
        ang_adj = ang_raw

    # Normalize to initial value
    curr_ang = int((ang_raw - ang_adj) * 100) / 100.0


if __name__ == '__main__':
    linear_adj = None
    ang_adj = None
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
        print("linear: %s\tangular: %s" % (curr_linear, curr_ang))
        rate.sleep()
