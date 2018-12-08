import csv
import numpy as np
from math import sin, cos, sqrt, atan2, radians
import math
from flask import Flask
app = Flask(__name__)

@app.route('/<location>')
def top_10(location):
	name=location.split(',')
	vals=[]
	with open("hotels.csv") as f:
		file=csv.reader(f,delimiter=',')
		for row in file:
			# print(row)
			if row[1]!="accommodation":
			# print(row)
				vals.append([row[1],row[2],row[5],row[6]])
			else:
				vals.append([row[6],row[0],row[3],row[4]])
	vals=np.array(vals)
	# print(vals[1,0])
	R = 6373.0
	results=[]
	for i in range(1,len(vals)):
		element=vals[i]
		lat1 = 51.526851
		lon1 = -0.098354
		lat1=float(name[0])
		lon1=float(name[1])
		lat2 = float(element[2])
		# print(lat2)
		lon2 = float(element[3])
		dlat = math.radians(lat2-lat1)
		dlon = math.radians(lon2-lon1)
		a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1))* math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
		c = 2 * atan2(math.sqrt(a), math.sqrt(1-a))
		distance = R * c
		results.append(distance)
	indices=np.argsort(results)
	# print(np.array(vals)[indices][:,1])
	top_5=np.array(vals)[indices][0:5,1] #1 is address
	top_5=np.array(vals)[indices][0:5,2:4] # returns lat and long
	return (str(top_5))
	#to get directions enter origin coordinates and destination coordinates from above :) 