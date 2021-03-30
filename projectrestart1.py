# Here I used memoization in attempt to shorten the calculation time of each iteration of the for loop

## Average Execution Time: 1.21ms
## Percent Improvement: 10.3%


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
	mLx = m*(L-x)
	hmk = h/(m*k)
	mL = m*L
	mx = m*x
	convective.append((a.cosh(mLx)+hmk*a.sinh(mLx))/(a.cosh(mL)+hmk*a.sinh(mL)))
	adiabatic.append((a.cosh(mLx))/(a.cosh(mL)))
	prescribed.append(((theta_l/theta_b)*a.sinh(mx)+a.sinh(mLx))/(a.sinh(mL)))
	infinite_fin.append(a.exp(-mx))
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
