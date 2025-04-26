import numpy as np
from scipy.optimize import linear_sum_assignment

# Profit matrix
profit = np.array([
    [16, 10, 14, 11],
    [14, 11, 15, 15],
    [15, 15, 13, 12],
    [13, 12, 14, 15]
])

# Convert to cost matrix for minimization
cost = profit.max() - profit

# Solve assignment
row, col = linear_sum_assignment(cost)

# Salesmen and Cities
salesmen = ['A', 'B', 'C', 'D']
cities = ['1', '2', '3', '4']

# Output
total_profit = 0
print("Assignment:")
for i in range(len(row)):
    print(f"Salesman {salesmen[row[i]]} -> City {cities[col[i]]} (Profit: {profit[row[i], col[i]]})")
    total_profit += profit[row[i], col[i]]

print(f"\n Total Maximum Profit = {total_profit} BDT")
