#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


def vels(dir, target_linear_vel, target_ang_vel):
    return "%s:\tlinear vel %s\t angular vel %s" % (dir, target_linear_vel, target_ang_vel)


def callback(msg):
    global pub, target_linear_vel, target_ang_vel, control_linear_vel, control_ang_vel

    if msg.axes[7] == 1.0:
        target_linear_vel = target_linear_vel + 0.01
        print vels("Forward ", target_linear_vel, target_ang_vel)
    elif msg.axes[7] == -1.0:
        target_linear_vel = target_linear_vel - 0.01
        print vels("Backward", target_linear_vel, target_ang_vel)
    elif msg.axes[6] == 1.0:
        target_ang_vel = target_ang_vel + 0.1
        print vels("Left    ", target_linear_vel, target_ang_vel)
    elif msg.axes[6] == -1.0:
        target_ang_vel = target_ang_vel - 0.1
        print vels("Right   ", target_linear_vel, target_ang_vel)
    elif msg.buttons[0] == 1 or msg.buttons[1] == 1 or msg.buttons[2] == 1 or msg.buttons[3] == 1:
        target_linear_vel = 0
        control_linear_vel = 0
        target_ang_vel = 0
        control_ang_vel = 0
        print vels("Stop", target_linear_vel, target_ang_vel)

    control_linear_vel = min(target_linear_vel,
                             control_linear_vel + (
                             0.01 / 4.0)) if target_linear_vel > control_linear_vel else target_linear_vel

    control_ang_vel = min(target_ang_vel,
                          control_ang_vel + (0.1 / 4.0)) if target_ang_vel > control_ang_vel else target_ang_vel

    twist = Twist()
    twist.linear.x = control_linear_vel
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = control_ang_vel
    pub.publish(twist)


target_linear_vel = 0
target_ang_vel = 0
control_linear_vel = 0
control_ang_vel = 0

rospy.init_node('xbox_remapper')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
sub = rospy.Subscriber('/joy', Joy, callback)
print "Listening..."

rospy.spin()
