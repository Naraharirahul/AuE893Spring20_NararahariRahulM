#! /usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from apriltag_ros.msg import AprilTagDetection
from apriltag_ros.msg import AprilTagDetectionArray
from geometry_msgs.msg import Point


def callback(data):
    # Acquire LiDAR data
    
	image_pub = rospy.Publisher("/tag_detections_image",Image,camera_callback)
	x_tag = data.detections[0].pose.pose.pose.position.x
	y_tag  = data.detections[0].pose.pose.pose.position.y
	z_tag = data.detections[0].pose.pose.pose.position.z
	print(x_tag,y_tag,z_tag)

	# Enter Controller
	move = Twist()

	
	# lateral error
	x_error = x_tag
	z_error = 0.3 - z_tag
	kp_ang = 0.5
	kp_lin = 0.3
	if abs(x_error) >= 0.1:
		move.angular.z = -kp_ang*x_error
	else:	
		move.angular.z = 0

	if abs(z_error) >= 0.1:
		move.linear.x = - kp_lin*z_error
	else:
		move.linear.x = 0
	# print(move.linear.x, move.angular.z)
	pub.publish(move)

rospy.init_node('detect_tag',anonymous=True)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
subscriber = rospy.Subscriber('/tag_detections',AprilTagDetectionArray,callback)
velocity_msg=Twist()
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(velocity_msg)
    rate.sleep()
    pass