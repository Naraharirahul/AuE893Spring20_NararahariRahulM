circle.py

For the circle.py code, I have used the rotate.py code from the turtlesim_cleaner package.
In this code I have provided the linear velocity in x diredction and as well as a angular velocity in z direction. 

The linear velocity is fixed to 10.
The angular velocity is computed by the formula = velocity/radius.
Once the user inputs the radius, the turtlebot will rotate around the given radius. 

square_openloop.py

For the square_openloop.py code, I have used both the roate.py as well as move.py code. Using these codes, the turtelbot will 
initially move to a distance the user mentions and then it rotates an angle of 90 degrees. 
To make the aboe process iterative, I have used for loop for it. Where for each iteration the distance is made zero and it will
move in that direction until it reaches the distance desired. 

The linear velocity in x direction is taken as 0.2
the angular velocity in z direction is taken as 0.2

square_closedloop.py

For the square_closedloop.py code, I have used gotogoal.py code as reference. Using that code, we can make the turtlebot to move to 
that position with a given angular speed. Using that code and the controller, I was able to move to a given point.

To make the turltebot move in square, I have used a for loop where initially the user shall enter the x,y coordinate to which the turtlesim has to move and then later on, it moves to the assigned coordinates. 


The videos are in the folder:
assignment2/src/assignment2/videos

The snapshots are in the folder:
assignment2/src/assignment2/snippets


