####!/usr/local/bin/python
import numpy as np
import matplotlib.pyplot as plt
import argparse


#
#    
#              N=0-deg   opp
#                      _______
#                     |       /  sin(theta) = opp/hyp
#                     |      /     - opp is our change in x-direction (dx)
#                    a|     /      - convert distance to travel (hyp) to grid units by dividing by 5 ft.
#                    d|    /p      - sum of n=1 to 3 of dxn + di = xf where dxn = dn/5ft * sin(thetan) 
#                    j|   /y
#        5ft          |  /h
#      |----|         | /
#                     |/ 
# |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
# 1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20
#

print
print "             _            _                 _                         _            _       _             " 
print "            (_)          | |               (_)                       | |          | |     | |            " 
print "   ___  _ __ _  ___ _ __ | |_ ___  ___ _ __ _ _ __   __ _    ___ __ _| | ___ _   _| | __ _| |_ ___  _ _ _" 
print "  / _ \| '__| |/ _ \ '_ \| __/ _ \/ _ \ '__| | '_ \ / _` |  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|"
print " | (_) | |  | |  __/ | | | ||  __/  __/ |  | | | | | (_| | | (_| (_| | | (__| |_| | | (_| | || (_) | |   "
print "  \___/|_|  |_|\___|_| |_|\__\___|\___|_|  |_|_| |_|\__, |  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   "
print "                                                     __/ |                                               "
print "                                                    |___/                                                "
print
print "              N=0-deg   opp                                                                              "
print "                       _______                                                                           "
print "                     |       /  sin(theta) = opp/hyp                                                     "
print "                     |      /     - opp is our change in x-direction (dx)                                "
print "                    a|     /      - convert distance to travel (hyp) to grid units by dividing by 5 ft.  "
print "                    d|    /p      - sum of n=1 to 3 of dxn + di = xf where dxn = dn/5ft * sin(thetan)    "
print "                    j|   /y                                                                              "
print "        5ft          |  /h                                                                               "
print "      |----|         | /                                                                                 "
print "                     |/                                                                                  "
print " |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|        "
print " 1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20        "



def parse_args(): #parse (interpret) command line arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--bearing",help="<Required> list of 3 integer bearings.",nargs=3,type=int,required=True)
    parser.add_argument("-d","--distance",help="<Required> list of 3 integer distances.",nargs=3,type=int,required=True)
    parser.add_argument("-g","--graph",help="<Optional> create a graph of the orienteering course path.",action="store_true")
    parser.add_argument("-s","--startpoint",help="<Required> this is the integer starting point.",type=int,required=True)
    return parser.parse_args()

args = parse_args() #call the pare_args function definition (actually perform the arg parse).

#get parameters from command line arguments
x0=args.startpoint
theta1,theta2,theta3=args.bearing[0],args.bearing[1],args.bearing[2]
dist1,dist2,dist3=args.distance[0],args.distance[1],args.distance[2]

#convert distance parameters to grid units by dividing by 5ft.
dist1=dist1/5.
dist2=dist2/5.
dist3=dist3/5.

#get points. There are 4. starting, first, second, and final destinations.
destinations=np.zeros(shape=(2,4)) # Initialized values to 0 [axis,coordinate]
destinations[0,0]=x0 #x coordinate starting position
destinations[1,0]=0  #y coordinate starting position
destinations[0,1]=dist1*np.sin(np.radians(theta1))+destinations[0,0] #x coordinate first location
destinations[1,1]=dist1*np.cos(np.radians(theta1))+destinations[1,0] #y coordinate first location
destinations[0,2]=dist2*np.sin(np.radians(theta2))+destinations[0,1] #x coordinate second location
destinations[1,2]=dist2*np.cos(np.radians(theta2))+destinations[1,1] #y coordinate second location
destinations[0,3]=np.round(dist3*np.sin(np.radians(theta3))+destinations[0,2]) #x coordinate final destination
destinations[1,3]=np.round(dist3*np.cos(np.radians(theta3))+destinations[1,2]) #y coordinate final destination

#solver
dx=dist1*np.sin(np.radians(theta1))+dist2*np.sin(np.radians(theta2))+dist3*np.sin(np.radians(theta3)) #change along x (the rope direction)
dy=dist1*np.cos(np.radians(theta1))+dist2*np.cos(np.radians(theta2))+dist3*np.cos(np.radians(theta3)) #change along y (perpendicular to rope)
print("beginning destination: "+str(int(np.round(x0))))   #print to screen the starting point.
print("correct destination: "+str(int(np.round(dx+x0))))  #print to screen the correct destination point.


if(args.graph):
   #make figure
   fig = plt.figure(1,figsize=(8,8))   #create 8 x 8 figure
   ax1 = fig.add_subplot(111)          #create single subplot area with axis ax1
   grid=np.arange(1,21,1)              #define grid.
   plt.xlim((-5,25))                   #Set x-axis range
   plt.ylim((0,25))                    #Set y-axis range
   
   # Draw rope and markers   [x1,x2]  [y1,y2]
   ax1.plot([1,20],[0,0],linewidth=3, color="black" )         #Rope 
   for i in grid:
       ax1.plot([i,i],[-0.25,0.25],linewidth=1,color="black") #Positional markers along rope.

   # Draw the course path
   ax1.plot(destinations[0],destinations[1],linewidth=2,color="red") #Trace path with lines.
   ax1.scatter(destinations[0],destinations[1],color="red")          #Mark locations with dots.
   plt.grid(True)                                                    #Show gridlines on plots.
   plt.gca().set_aspect('equal',adjustable='box')                    #Set x and y axes to be proportional.
   plt.title('Starting point: %d \n %d feet @ %d degrees \n %d feet @ %d degrees \n %d feet @ %d degrees \n Ending point: %d'\
              % (x0,dist1*5,theta1,dist2*5,theta2,dist3*5,theta3,int(np.round(dx+x0)))) #Figure title
   plt.savefig("./compass_course.png")                               #Save figure.
   plt.show()                                                        #Distplay figure after saving.
