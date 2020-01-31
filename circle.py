#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    print("Let's move your robot")
    radius = input("Type your radius:")
    distance = 100	
    speed = 10
    vel_msg.linear.x = 10
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = speed/radius
    while not rospy.is_shutdown():
        
        t0 = float(rospy.Time.now().to_sec())
        current_distance = 0
      
        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=float(rospy.Time.now().to_sec())
            current_distance= speed*(t1-t0)
        vel_msg.linear.x = 0      
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        
        move()
    except rospy.ROSInterruptException: pass
