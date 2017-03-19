import math
import random

def hypothesis(x,theta):
	#input("In hypothesis")
	#print "In hypothesis()"
	return float(x * theta)

def costFunction(m,theta,features,target):
	#print "In costFunction()"
	error = 0
	index = 0
	er = 0
	for item in features:
		er = hypothesis(item,theta) - target[index]
		index = index + 1
		error = error + pow(er,2)	
	return (error / (2.0 * m))

def minimize(thetas, m, features, target):
	#print "In minimize()"
	minTheta = []
	for theta in thetas:
		jOfTheta = costFunction(m,theta,features,target)
		print "theta: ", theta, jOfTheta
		minTheta.append(jOfTheta)
	return minTheta

def generateData(start, stop, step, features):
	data=[]
	for i in range(features):
		data.append(random.randrange(start,stop,step))
	return data


# Generate 4000 random "Area of house" features
# and return the generated list.
# Elements are in following manner
# Element 1-1000 : random elemnts in range 600 to 900 in step of 10
# Element 1-1000 : random elemnts in range 900 to 1500 in step of 10
# Element 1-1000 : random elemnts in range 1500 to 2000 in step of 10
# Element 1-1000 : random elemnts in range 2000 to 4000 in step of 10

def generateDataBlocks(n=4000,bounds=[600,900,1500,2000,4000],step=10):
	data = []
	block = int(n/(len(bounds)-1))
	for j in range(len(bounds)-1):
		data = data + generateData(bounds[j],bounds[j+1],step,block)
	return data


def foo():
	print "in foo"
	j = bar()
	print "end foo"
	return j

def bar():
	print "in bar"
	print "end bar"
	return 234
