#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        
    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance
        

    def move2goal(self):
        
        print("Let's go")
        positions = [[0,0],[0,0],[0,0],[0,0],[0,0]]
        goal_pose = Pose()

        for i in range (0,5):
	    goal_pose.x = input("Set your X goal: ")
            goal_pose.y = input("Set your Y goal: ")
	    positions[i][0] = goal_pose.x
	    positions[i][1] = goal_pose.y
	
        distance_tolerance = input("Set your tolerance:")
        vel_msg = Twist()


	for j in range (0,5):
      	
            while abs((atan2(positions[j][1] - self.pose.y, positions[j][0] - self.pose.x) - self.pose.theta)) >= 0.001:
            
	    #angular velocity in the z-axis:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 2 * (atan2(positions[j][1] - self.pose.y, positions[j][0] - self.pose.x) - self.pose.theta)

            #Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()
	    

	    while  sqrt(pow((positions[j][0] - self.pose.x), 2) + pow((positions[j][1] - self.pose.y), 2)) >= distance_tolerance:

            #Porportional Controller
            #linear velocity in the x-axis:
                vel_msg.linear.x = 2 * sqrt(pow((positions[j][0] - self.pose.x), 2) + pow((positions[j][1] - self.pose.y), 2))
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.z = 0

              #Publishing our vel_msg
 	        self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

          
        #Stopping our robot after the movement is over
            vel_msg.linear.x = 0
            vel_msg.angular.z =0
            self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move2goal()

    except rospy.ROSInterruptException: pass
