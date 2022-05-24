import numpy as np
import matplotlib.pyplot as plt

# degrees to radian converter
def mm_to_m(T):
    m=1000
    return d/m

# Variables
di = float(input('di = ')) #initial position
di = mm_to_m(di)

di = float(input('di = ')) #initial velocity
di = mm_to_m(di)

df = float(input('df = ')) #final position
df = mm_to_m(df)

df = float(input('df = ')) #final velocity
df = mm_to_m(df)

ti = float(input('ti = ')) #initial time
tf = float(input('tf = ')) #final time

# Cubic Equation
# Solve the solution for q(t) = a + ((3*(b-a)/c**2)*(t**2)) - ((2*(b-a)/c**3)*(t**3))

x = np.arange(ti,tf,0.05) # x axis (time axis)

def cubic(t,a,b,c):
    return a + ((3*(b-a)/c**2)*(t**2)) - ((2*(b-a)/c**3)*(t**3))

y = cubic(x,di,df,tf)

plt.figure()
plt.plot(x,y,'g', linestyle='-')
plt.text(1,1.5,'q(t) = a + ((3*(b-a)/c**2)*(t**2)) - ((2*(b-a)/c**3)*(t**3))')
plt.grid(True)
plt.show()