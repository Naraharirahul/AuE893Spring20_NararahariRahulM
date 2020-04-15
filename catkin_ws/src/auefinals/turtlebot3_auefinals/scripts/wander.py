#! /usr/bin/env python

import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
PI = 3.1415926535897


def callback(data): 
    left_sweep = data.ranges[45:90]
    right_sweep = data.ranges[270:315]    
    # front_sweep1 = data.ranges[315:359]  
    front_sweep = data.ranges[0:45]
    # front-sweep = front_sweep1[315:359] + front_sweep2[0:45]

    avgr = sum(right_sweep)/len(right_sweep)
    avgf = sum(front_sweep)/len(front_sweep)
    avgl = sum(left_sweep)/len(left_sweep)

    if avgf > 5 or avgf< -5:
        avgf = min(front_sweep)
    if avgr > 5 or avgr < -5:
        avgr = min(right_sweep)
    if avgl > 5 or  avgl < -5:
        avgl = min(left_sweep)

    kp = 0.7
    
    if avgl > avgr and avgf:
        velocity_msg.linear.x = 0.1
        velocity_msg.angular.z = 0.8

    if avgf > avgl and avgr:
        velocity_msg.linear.x = 0.1
        velocity_msg.angular.z = 0
        
    if avgr > avgl and avgf:
        velocity_msg.linear.x = 0.1
        velocity_msg.angular.z = -0.8

    

rospy.init_node('turtle_control', anonymous=True)
velocity_msg=Twist()
pub = rospy.Publisher('cmd_vel', Twist, queue_size= 10)
sub = rospy.Subscriber('scan', LaserScan,callback)
rate = rospy.Rate(15)

while not rospy.is_shutdown():
    pub.publish(velocity_msg)
    rate.sleep()
