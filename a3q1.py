import numpy as np
from scipy.integrate import odeint,solve_ivp
import matplotlib.pyplot as plt

def ode1(t,y):
    return t*np.exp(3*t) - 2*y
def ode2(t,y):
    return 1 + (t-y)**2
def exact1(t):
    return (1/5)*t*np.exp(3*t) - (1/25)*np.exp(3*t) + (1/25)*np.exp(-2*t)
def exact2(t):
    return t + 1/(1-t)

tspan1 = (0,1)
y0_1 = 0
t_eval1 = np.linspace(0,1,100)

tspan2 = (2,3)
y0_2 = 1
t_eval2 = np.linspace(2,3,100)

sol_odeint1 = odeint(lambda y,t: ode1(t,y), y0_1, t_eval1)
sol_odeint2 = odeint(lambda y,t: ode2(t,y), y0_2, t_eval2)

sol_ivp1 = solve_ivp(ode1,tspan1,[y0_1],t_eval=t_eval1)
sol_ivp2 = solve_ivp(ode2,tspan2,[y0_2],t_eval=t_eval2)

exact_sol1 = exact1(t_eval1)
exact_sol2 = exact2(t_eval2)

error_odeint1 = np.abs(sol_odeint1[:,0] - exact_sol1)
error_ivp1 = np.abs(sol_ivp1.y[0] - exact_sol1)

error_odeint2 = np.abs(sol_odeint2[:,0] - exact_sol2)
error_ivp2 = np.abs(sol_ivp2.y[0] - exact_sol2)


print("Errors for the first ODE:")
print("odeint:", error_odeint1)
print("solve_ivp:", error_ivp1)

print("Errors for the second ODE:")
print("odeint:", error_odeint2)
print("solve_ivp:", error_ivp2)


plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.plot(t_eval1, sol_odeint1[:,0], label='odient')
plt.plot(t_eval1, sol_ivp1.y[0], label='Solve_ivp')
plt.plot(t_eval1, exact_sol1, label='Exact Solution', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution for (i)')
plt.legend()


plt.subplot(2,1,2)
plt.plot(t_eval2, sol_odeint2[:,0], label='odient')
plt.plot(t_eval2, sol_ivp2.y[0], label='Solve_ivp')
plt.plot(t_eval2, exact_sol2, label='Exact Solutin', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution for (ii)')
plt.legend()

plt.tight_layout()
plt.show()