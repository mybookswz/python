import numpy as np
import matplotlib.pyplot as plt


r = 0.0433

years = np.array([1,2,3,4,5])
investment_A = np.array([225,215,250,225,205])
investment_B = np.array([220,225,250,250,210])

PV_A = np.sum(investment_A * np.exp(- r * years))
PV_B = np.sum(investment_B * np.exp(- r * years))

print(f"Present Value of Investment A : {PV_A:.2f}")
print(f"Present Value of Investment B : {PV_B:.2f}")

if PV_A > PV_B:
    print("Investment A is Preferable")
elif PV_B > PV_A:
    print("Investment B is Preferable")
else:
    print("Both are equally Preferable")
