import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lotka_volterra(t,z):
    x,y = z
    dxdt = -0.1*x + 0.02*x*y 
    dydt = 0.2*y - 0.025*x*y 
    return [dxdt,dydt]

z0 = [6,6]
tspan = (0,50)

sol = solve_ivp(lotka_volterra,tspan,z0,t_eval=np.linspace(0,50,500))

x = sol.y[0]
y = sol.y[1]
t = sol.t

plt.plot(t,x,label='Predators(x)')
plt.plot(t,y,label='Prey(y)')
plt.xlabel('Time')
plt.ylabel('Populations (thousands)')
plt.title('Predators & prey ')
plt.grid(True)
plt.show()

for i in range(1,len(t)):
    if abs(x[i]-y[i])<0.1:
        print(f'The first time when two populations are equal t = {t[i]:}')
        break 