import numpy as np
from scipy.optimize import linprog

c = np.array([4, 3])

A = np.array([
    [-200, -100],  # Vitamins: 200x1 + 100x2 >= 4000 → -200x1 - 100x2 <= -4000
    [-1,    -2],   # Minerals: x1 + 2x2 >= 50 → -x1 - 2x2 <= -50
    [-40,   -40]   # Calories: 40x1 + 40x2 >= 1400 → -40x1 - 40x2 <= -1400
])

b = np.array([-4000, -50, -1400])

result = linprog(c, A_ub=A, b_ub=b, method='highs')

if result.success:
    x1, x2 = result.x
    min_cost = result.fun
    print("Optimal Solution:")
    print(f"Units of Food A (x1): {x1:.2f}")
    print(f"Units of Food B (x2): {x2:.2f}")
    print(f"Minimum Cost: {min_cost:.2f} BDT")
else:
    print("No feasible solution found.")
