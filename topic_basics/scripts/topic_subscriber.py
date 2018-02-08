#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):
    print("Msg: {} ".format(msg.data))


def callback_with_user_data(msg, cb_args):
    print("Msg: {} CB args: {} ".format(msg.data, cb_args))


def main():
    # Initialize node
    rospy.init_node('topic_subscriber')

    # Setup subscriber without callback args
    rospy.Subscriber('counter', Int32, callback=callback)

    # Setup subscriber without callback args
    rospy.Subscriber('counter', Int32, callback=callback_with_user_data, callback_args="callback1")
    rospy.Subscriber('counter', Int32, callback=callback_with_user_data, callback_args="callback2")

    print("Listening...")
    # Wait
    rospy.spin()


if __name__ == '__main__':
    main()
