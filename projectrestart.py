# The premise of this code (and the following files) was to compare heat transfer models to actual heat transfer data from thermocouples
# Specifically, a cirular rod (diameter D and length L) acts as a fin from a hot water tank
# This code shows the models' prediction of the temperature profile along the length of the rod


## This is the recreation of the my first attempt at coding my ME70 Lab 1 in Python, I used only my basic knowledge of python

### Average Completion Time: 1.35ms

import time
import math as a

start_time = time.time()

ItoM = .0254 #inches to meter conversion
CtoK = 273 #Celcius to Kelvin

L = 16*ItoM #Length
dx = 2*ItoM #thermocouple spacing
D = .3822*ItoM
P = a.pi*D
A = a.pi*(D**2)/4
locations_meters = []
for i in range(100):
	locations_meters.append(((i+1)/100)*L)

#print("locations_meters[99]: " + str(locations_meters[99]))
#print("L: " + str(L))

k = 109
h = 8.33732 #Using average temp of rod = 50C and ambient temp = 21, online calc
m = a.sqrt((h*P)/(k*A))
Tb = 70.5+CtoK
Tl = 22.8+CtoK
Tinf = 20.5+CtoK
theta_b = Tb-Tinf
theta_l = Tl-Tinf

convective = []
adiabatic = []
prescribed = []
infinite_fin = []
locations_inches = []
# in terms of theta/theta_b
for x in locations_meters:
	convective.append((a.cosh(m*(L-x))+(h/(m*k))*a.sinh(m*(L-x)))/(a.cosh(m*L)+(h/(m*k))*a.sinh(m*L)))
	adiabatic.append((a.cosh(m*(L-x)))/(a.cosh(m*L)))
	prescribed.append(((theta_l/theta_b)*a.sinh(m*x)+a.sinh(m*(L-x)))/(a.sinh(m*L)))
	infinite_fin.append(a.exp(-m*x))
	locations_inches.append(x/ItoM)

convective_data = []
adiabatic_data = []
prescribed_data = []
infinite_fin_data = []
#converting to Temperatures
for x in range(len(convective)):
	convective_data.append((convective[x]*theta_b+Tinf)-CtoK)
	adiabatic_data.append((adiabatic[x]*theta_b+Tinf)-CtoK)
	prescribed_data.append((prescribed[x]*theta_b+Tinf)-CtoK)
	infinite_fin_data.append((infinite_fin[x]*theta_b+Tinf)-CtoK)

thermocouple_data = [56.7458,46.7435,38.4084,32.9954,28.5892,26.5125,25.5397]
x_loc = [2,4,6,8,10,12,14]

#print(convective)
#print(convective_data)

total_time = (time.time()-start_time)*1000
print("Time for completion in Milliseconds: " + str(total_time))
