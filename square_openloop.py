#!/usr/bin/env python
import rospy
from geometry_msgs.msg   import Twist
from math import radians
PI = 3.1415926

def move():
    
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    distance = input("Type your length of the side:")   

    for i in range(0,4):
    	
    	speed = 2
    	vel_msg.linear.x  = 2
    	vel_msg.linear.y = 0
    	vel_msg.linear.z = 0
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0
    	   
      
      	

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        
        while(current_distance < distance):
	               
            velocity_publisher.publish(vel_msg)
            t1=(rospy.Time.now().to_sec())
            current_distance= speed*(t1-t0) 
        vel_msg.linear.x = 0
	velocity_publisher.publish(vel_msg)
	t0a = (rospy.Time.now().to_sec())
	current_angle = 0	
        angular_speed = 90* 2* PI / 360
        relative_angle = 90* 2* PI / 360
        vel_msg.angular.z = 2
	while(current_angle < relative_angle): 
             
             velocity_publisher.publish(vel_msg)
             t1a = rospy.Time.now().to_sec()
             current_angle = 2*(t1a - t0a)
             

    	vel_msg.angular.z = 0
    	velocity_publisher.publish(vel_msg)
        
       
 

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
