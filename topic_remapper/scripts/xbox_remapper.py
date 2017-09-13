#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


def vels(target_linear_vel, target_angular_vel):
    return "currently:\tlinear vel %s\t angular vel %s " % (target_linear_vel, target_angular_vel)

def callback(msg):
    global pub, target_linear_vel, target_angular_vel, control_linear_vel, control_angular_vel
    if msg.axes[6] != 0.0 or msg.axes[7] != 0.0:
        print("Remapping {0} {1}".format(msg.axes[6], msg.axes[7]))

    if msg.axes[7] == 1.0:
        target_linear_vel = target_linear_vel + 0.01
        print vels(target_linear_vel, target_angular_vel)
    elif msg.axes[7] == -1.0:
        target_linear_vel = target_linear_vel - 0.01
        print vels(target_linear_vel, target_angular_vel)
    elif msg.axes[6] == 1.0:
        target_angular_vel = target_angular_vel + 0.1
        print vels(target_linear_vel, target_angular_vel)
    elif msg.axes[6] == -1.0:
        target_angular_vel = target_angular_vel - 0.1
        print vels(target_linear_vel, target_angular_vel)
    elif msg.buttons[0] == 1 or msg.buttons[1] == 1 or msg.buttons[2] == 1 or msg.buttons[3] == 1:
        print("Stopping")
        target_linear_vel = 0
        control_linear_vel = 0
        target_angular_vel = 0
        control_angular_vel = 0
        print vels(target_linear_vel, target_angular_vel)

    if target_linear_vel > control_linear_vel:
        control_linear_vel = min(target_linear_vel, control_linear_vel + (0.01 / 4.0))
    else:
        control_linear_vel = target_linear_vel

    if target_angular_vel > control_angular_vel:
        control_angular_vel = min(target_angular_vel, control_angular_vel + (0.1 / 4.0))
    else:
        control_angular_vel = target_angular_vel

    twist = Twist()
    twist.linear.x = control_linear_vel
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = control_angular_vel
    pub.publish(twist)

target_linear_vel = 0
target_angular_vel = 0
control_linear_vel = 0
control_angular_vel = 0

rospy.init_node('xbox_remapper')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
sub = rospy.Subscriber('/joy', Joy, callback)
print "Listening..."

rospy.spin()
