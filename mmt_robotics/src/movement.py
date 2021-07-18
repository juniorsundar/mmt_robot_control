#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import random

def mover():
    joint1 = rospy.Publisher('/ur5e/joint1_position_controller/command', Float64, queue_size=10)
    joint2 = rospy.Publisher('/ur5e/joint2_position_controller/command', Float64, queue_size=10)
    joint3 = rospy.Publisher('/ur5e/joint3_position_controller/command', Float64, queue_size=10)
    joint4 = rospy.Publisher('/ur5e/joint4_position_controller/command', Float64, queue_size=10)
    joint5 = rospy.Publisher('/ur5e/joint5_position_controller/command', Float64, queue_size=10)
    joint6 = rospy.Publisher('/ur5e/joint6_position_controller/command', Float64, queue_size=10)

    rospy.init_node('commander', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        joint1.publish(-2*random.random())
        joint2.publish(-2*random.random())
        joint3.publish(-2*random.random())
        joint4.publish(-2*random.random())
        joint5.publish(-2*random.random())
        joint6.publish(-2*random.random())
        rate.sleep()

if __name__ == '__main__':
    try:
        random.seed()
        mover()
    except rospy.ROSInterruptException:
        pass 