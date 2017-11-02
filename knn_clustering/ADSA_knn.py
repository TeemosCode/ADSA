import matplotlib.pyplot as plt 
import numpy as np 
import random
import math

# For N (different numbers), More generalized for different number of clusters 

#returns a tuple of two lists 
def data_gen():
	x=list()
	y=list() 
	for i in range(500):
		x.append(random.randint(0,600))
		y.append(random.randint(0,600))
	for i in range(500):
		x.append(random.randint(400,1000))
		y.append(random.randint(400,1000))
	return (x,y)



# takes 2 arrays as input of X and corresponding Y
# Returns the mean 
def mean_calculator(x,y):
	x_m=0
	y_m=0
	for i in range(len(x)):
		x_m+=x[i]
		y_m+=y[i]
	return (((x_m)/len(x)),((y_m)/len(y)))


# Passed in is a tuple of 6 values 
# Returns the eval function ( avg dist values ) for both clusters
def eval_func(i):
	x1=i[2]
	x2=i[4]
	y1=i[3]
	y2=i[5]
	m1=mean_calculator(x1,y1)
	m2=mean_calculator(x2,y2)
	total=0
	total2=0
	for j in range(len(x1)):
		total+=distance_calculator((x1[j],y1[j]),m1)
	for j in range(len(x2)):
		total2+=distance_calculator((x2[j],y2[j]),m2)
	return ((total/len(x1)),(total2/len(x2)))

# takes two tuples of coordinates as input
# returns the distance betweeen the two points  
def distance_calculator(p1,p2):
	return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


# main function to perform clustering 
def cluster():

# Declaring all required cluster variables to hold the two different clusters 
	c1_x=list()
	c1_y=list()

	c2_y=list()
	c2_x=list()

# Generating required data
	data=data_gen()
	x=data[0]
	y=data[1]

# Array to keep track of starting positions and all the respective clusters
	arr=list()

# Looping through to get 100 different sets of random starting points 
	for l in range(100):

# initialising the randomised starting points
		in1=random.randint(0,len(x))
		in2=random.randint(0,len(x))
		s1=x[in1],y[in1]
		s2=x[in2],y[in2]
		t1=s1
		t2=s2
# Array to keep track of which number belongs to which cluster 
		k=[0 for i in range (1000)]

# Loop to run 100 iterations of our algorithm 
		for i in range(100):

# Looping through all the points in our dataset to assign them to a cluster 
			for j in range(1000):

# Calculating the distance from the current point to the two means 
				d1=distance_calculator(s1,(x[j],y[j]))
				d2=distance_calculator(s2,(x[j],y[j]))

# Assigning the point a cluster based on whhich mean is closer 
				if(d1>d2):
					k[j]=2
				else:
					k[j]=1

# Clearing out previous clusters 
			del c1_y
			del c1_x
			del c2_x
			del c2_y

# Initialising the new clusters based on the k array value 
			c1_x=[x[i] for i in range(len(x)) if(k[i]==1)]
			c1_y=[y[i] for i in range(len(x)) if(k[i]==1)]
			c2_x=[x[i] for i in range(len(x)) if(k[i]==2)]
			c2_y=[y[i] for i in range(len(x)) if(k[i]==2)]

# Calculating the mean of the new clusters 
		s1=mean_calculator(c1_x,c1_y)
		s2=mean_calculator(c2_x,c2_y)

# Adding the starting conditions and the mean to the list of all models as a 6 value tuple 
		arr.append((t1,t2,c1_x,c1_y,c2_x,c2_y))

# Checking which model has best eval func value 		
	mini=1000
	ans=0
# Looping through all starting points and their respective clusters
	for i in arr:
# Getting average distance of points based on the eval function 
		cur_e=eval_func(i)
# Getting the difference between the size of both the clcusters 
		cur_diff=math.fabs(len(i[2])-len(i[4]))
		cur_eval=cur_e[0]+cur_e[1]
# Final eval function used is a weighted superposition of the average dist form mean 
# + 2 times the difference in size of the clusters
		if((cur_eval+cur_diff*2)<mini):
			mini=cur_eval+cur_diff*2
			ans=i
# Plotting the clusters as well as the two starting points and showing the graph 
	plt.plot(ans[2],ans[3],'r.',ans[4],ans[5],'g.')
	plt.plot([ans[0][0],ans[1][0]],[ans[0][1],ans[1][1]],'ro')
	plt.show()
	print("the starting points were",ans[0],ans[1])


# Calling the cluster function
cluster()