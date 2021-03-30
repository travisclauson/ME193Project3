# Here I used the Numpy Library to perform vector math (instead of for loops)

## Average Execution Time: .62ms
## Percent Improvement: 54.1%

import time
import math as a #since I am using a variable 'm'
import numpy as np

start_time = time.time()

ItoM = .0254 #inches to meter conversion
CtoK = 273 #Celcius to Kelvin

L = 16*ItoM #Length
dx = 2*ItoM #thermocouple spacing
x = np.linspace(0,L,100) #100 data points per thermocouple
D = .3822*ItoM
P = np.pi*D
A = np.pi*(D**2)/4

k = 109
h = 8.33732 #Using average temp of rod = 50C and ambient temp = 21, online calc
m = a.sqrt((h*P)/(k*A))
Tb = 70.5+CtoK
Tl = 22.8+CtoK
Tinf = 20.5+CtoK
theta_b = Tb-Tinf
theta_l = Tl-Tinf

mL = m*L
hmk = h/(m*k)

# in terms of theta/theta_b
# have to use numpy instead of math to calculate the sinh/cosh of all values in an array
convective = (np.cosh(m*(L-x))+hmk*np.sinh(m*(L-x)))/(np.cosh(mL)+hmk*np.sinh(m*L))
adiabatic = (np.cosh(m*(L-x)))/(np.cosh(mL))
prescribed = ((theta_l/theta_b)*np.sinh(m*x)+np.sinh(m*(L-x)))/(np.sinh(mL))
infinite_fin = np.exp(-m*x)

convective_data = (convective*theta_b+Tinf)-CtoK
adiabatic_data = (adiabatic*theta_b+Tinf)-CtoK
prescribed_data = (prescribed*theta_b+Tinf)-CtoK
infinite_fin_data = (infinite_fin*theta_b+Tinf)-CtoK
x_inches = x/ItoM

thermocouple_data = np.array([56.7458,46.7435,38.4084,32.9954,28.5892,26.5125,25.5397])
x_loc = np.array([2,4,6,8,10,12,14])

total_time = (time.time()-start_time)*1000
print("Time for completion in Milliseconds: " + str(total_time))
