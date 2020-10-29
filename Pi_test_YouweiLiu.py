# funtion to determine whether the point (x,y) is in the circle with r radius
# return ture if is in the circle, false if is on or out of the circle
def circle(x,y,r):
    r=abs(r)    #make sure the r is valid
    if pow(x,2) + pow(y,2) < pow(r,2):
        return True
    else:
        return False
    
# (x,y) is the upper right point of the partition square
# r is the side length of the square and the radius of the circle
# levelmax decide how many levels will the partition will end on
# level decide the current partition level, 0 means partition for square with diagonal (0,0) to (x,y)
        
# the algorithm use recursion as main idea
# the idea is based on calculus, for every partition it seperate the previous partition cells into 4 more partition cell, 
# until there the cell is all contained in the circle, or reach the require partition depth
# if the cell contains part of the circle, the area will be count half into the calculation
# it is more effectient in a way that if do not need to go though every single portion in iteration
def partition(x,y,r,levelmax, level):
    x=abs(x)
    y=abs(y)
    
    #exceptions
    if  levelmax<1:
        print("ERROR! invalid partition level")
        return 0
    
    #if the upper right point of the partition is in the circle, return the area, stop recursion to save computation power
    elif circle(x,y,r):
        return pow(r,2)/pow(2,level*2)
    
    elif (not circle(x,y,r)) and level<levelmax:
        level+=1
        return partition(x,y,r,levelmax, level)+partition(x-r/pow(2,level),y-r/pow(2,level),r,levelmax,level)+partition(x-r/pow(2,level),y,r,levelmax,level)+partition(x,y-r/pow(2,level),r,levelmax,level)
    
    #if the upper right point is not in the circle, but the down left point is in circle, return half of the area to do a average of high and low partition
    elif circle(x-r/pow(2,level),y-r/pow(2,level),r):
        return 0.5*pow(r,2)/pow(2,level*2)
    
    #if neither this 2 point is in the circle, return 0
    else:
        return 0


levelmax=12
print("Note: for every computation level added the error will reduce by a factor of 2")
print("Current computation precision level is",levelmax,"\n")

# the circle with radius 2, in first quadrant has the area Pi, the higher the levelmax, the higher the precision
Pi=partition(2,2,2,levelmax,0)



#Testing function(assume real pi value is not availible)
#this function will show the lower limit of the pi value
def partition_down(x,y,r,levelmax, level):
    x=abs(x)
    y=abs(y)
    
    #exceptions
    if  levelmax<1:
        print("ERROR! invalid partition level")
        return 0
    
    #if the upper right point of the partition is in the circle, return the area, stop recursion to save computation power
    elif circle(x,y,r):
        return pow(r,2)/pow(2,level*2)
    
    elif (not circle(x,y,r)) and level<levelmax:
        level+=1
        return partition_down(x,y,r,levelmax, level)+partition_down(x-r/pow(2,level),y-r/pow(2,level),r,levelmax,level)+partition_down(x-r/pow(2,level),y,r,levelmax,level)+partition_down(x,y-r/pow(2,level),r,levelmax,level)

    
    #if the square is not fully contained in the circle,then return 0
    else:
        return 0

import math
Pi_lower=partition_down(2,2,2,levelmax,0)
error=100*(Pi-Pi_lower)/Pi
digit=int(levelmax/3)+2
#print("the lower limit of Pi is estimate as",round(Pi_lower,digit))
print("Pi is estimate as\n",round(Pi,digit),"+-",round(Pi-Pi_lower,digit),"\n")
print("Estimate error is below",round(error,digit-1),"%")


realerr=abs(100*(Pi-math.pi)/math.pi)
print("The error respect to the real Pi is",round(realerr,digit),"%" )
