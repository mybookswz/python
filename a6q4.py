import numpy as np

#(a)
r = 0.1
T = 1
S0 = 40

F = S0 * np.exp(r * T)
Initial_val = 0

print(f"(a) Forward Price is : {F:.2f}")
print(f"Value of forward contract(initial) : {Initial_val:.2f}")

#(b)
St = 45
t = 0.5
time_remaining = T - t

Ft = St * np.exp(r * time_remaining)
Vt = St - F * np.exp(-r * time_remaining)

print(f"\n(b) Forward Price is after 6 month : {Ft:.2f}")
print(f"Value of forward contract after 6 month : {Vt:.2f}")
