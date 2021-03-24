import math
# ask the user to input the points
x1, y1 = input("enter values for the first point (x,y), Seperated by a single space \n").split()
x2, y2 = input("enter the values for the second point (x,y), Seperated by a single space \n").split()
# convert the values obtained from string to integer
int_of_X1 = int(x1)
int_of_Y1 = int(y1)
int_of_X2 = int(x2)
int_of_Y2 = int(y2)
# do the computations
# 1 get the difference
x_diff = (int_of_X2-int_of_X1)
y_diff = (int_of_Y2-int_of_Y1)
# 2 get the square
x_square = x_diff**2
y_square = y_diff**2
#add the values
added_value=x_square + y_square
# get the square root
distance = math.sqrt(added_value)
print("The distance is ", distance)