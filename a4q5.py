import numpy as np
import pandas as pd

# Problem data
costs = np.array([
    [4, 3, 1, 2, 6],  # A
    [5, 2, 3, 4, 5],  # B
    [3, 5, 6, 3, 2],  # C
    [2, 4, 4, 5, 3]   # D
])

supply = np.array([80, 60, 40, 20])
demand = np.array([60, 60, 30, 40, 10])

# North-West Corner Method
def north_west_corner(supply, demnd):
    supply_copy = supply.copy()
    demand_copy = demnd.copy()
    m, n = len(supply_copy), len(demand_copy)
    allocation = np.zeros((m, n))
    
    i, j = 0, 0
    while i < m and j < n:
        quantity = min(supply_copy[i], demand_copy[j])
        allocation[i, j] = quantity
        supply_copy[i] -= quantity
        demand_copy[j] -= quantity
        
        if supply_copy[i] == 0:
            i += 1
        if demand_copy[j] == 0:
            j += 1
    
    return allocation

nw_allocation = north_west_corner(supply, demand)
nw_cost = np.sum(nw_allocation * costs)

# Least Cost Method
def least_cost_method(costs, supply, demand):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    m, n = costs.shape
    allocation = np.zeros((m, n))
    
    while np.sum(supply_copy) > 0 and np.sum(demand_copy) > 0:
        # Find the cell with minimum cost among remaining cells
        min_val = np.inf
        min_i, min_j = -1, -1
        
        for i in range(m):
            if supply_copy[i] == 0:
                continue
            for j in range(n):
                if demand_copy[j] == 0:
                    continue
                if costs[i, j] < min_val:
                    min_val = costs[i, j]
                    min_i, min_j = i, j
        
        if min_i == -1:  # No cell found
            break
            
        quantity = min(supply_copy[min_i], demand_copy[min_j])
        allocation[min_i, min_j] = quantity
        supply_copy[min_i] -= quantity
        demand_copy[min_j] -= quantity
    
    return allocation

lc_allocation = least_cost_method(costs, supply, demand)
lc_cost = np.sum(lc_allocation * costs)

# Visualization
def print_allocation(allocation, method_name, total_cost):
    print(f"\n{method_name} Allocation:")
    df = pd.DataFrame(allocation, 
                      index=['A', 'B', 'C', 'D'], 
                      columns=['P', 'Q', 'R', 'S', 'T'])
    print(df)
    print(f"Total Cost: {total_cost}")

print_allocation(nw_allocation, "North-West Corner Method", nw_cost)
print_allocation(lc_allocation, "Least Cost Method", lc_cost)
