#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def main():
    # Initialize node
    rospy.init_node('topic_publisher')

    # Setup publisher
    pub = rospy.Publisher('counter', Int32, queue_size=10)

    # Create a rate
    rate = rospy.Rate(2)
    count = 0

    # Publish values
    while not rospy.is_shutdown():
        print("Publishing: " + str(count))
        pub.publish(count)
        count += 1
        rate.sleep()


if __name__ == '__main__':
    main()
