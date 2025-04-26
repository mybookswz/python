import numpy as np
import pandas as pd

# Define data
cost = np.array([
    [16, 20, 12],
    [14, 8, 18],
    [26, 24, 16]
])

supply = [200, 160, 90]
demand = [180, 120, 150]

# Balance the problem
if sum(supply) > sum(demand):
    cost = np.hstack((cost, np.zeros((cost.shape[0], 1))))
    demand.append(sum(supply) - sum(demand))
elif sum(supply) < sum(demand):
    cost = np.vstack((cost, np.zeros((1, cost.shape[1]))))
    supply.append(sum(demand) - sum(supply))

# Initial solution using North-West Corner Method
def north_west_corner(supply, demand):
    supply = supply.copy()
    demand = demand.copy()
    m, n = len(supply), len(demand)
    x = np.zeros((m, n))
    i = j = 0
    while i < m and j < n:
        val = min(supply[i], demand[j])
        x[i, j] = val
        supply[i] -= val
        demand[j] -= val
        if supply[i] == 0:
            i += 1
        else:
            j += 1
    return x

# MODI method
def modi_method(cost, initial_solution):
    m, n = cost.shape
    x = initial_solution.copy()

    while True:
        # Step 1: Find u and v
        u = [None] * m
        v = [None] * n
        u[0] = 0  # set u0 = 0
        while None in u or None in v:
            for i in range(m):
                for j in range(n):
                    if x[i, j] > 0:
                        if u[i] is not None and v[j] is None:
                            v[j] = cost[i, j] - u[i]
                        elif v[j] is not None and u[i] is None:
                            u[i] = cost[i, j] - v[j]
        
        # Step 2: Find opportunity cost
        delta = np.full((m, n), None)
        for i in range(m):
            for j in range(n):
                if x[i, j] == 0:
                    delta[i, j] = cost[i, j] - (u[i] + v[j])

        min_delta = np.min([d for row in delta for d in row if d is not None])

        if min_delta >= 0:
            # Optimal solution found
            break

        # Step 3: Find cell with most negative delta
        min_pos = np.argwhere(delta == min_delta)[0]
        i, j = min_pos

        # Find a loop (stepping stones method)
        marked = np.zeros_like(x)
        marked[i, j] = 1

        def find_loop(path):
            if len(path) >= 4 and path[0] == path[-1]:
                return path
            i, j = path[-1]
            for k in range(len(x)):
                if x[i, k] > 0 and (i, k) not in path:
                    new_path = find_loop(path + [(i, k)])
                    if new_path:
                        return new_path
                if x[k, j] > 0 and (k, j) not in path:
                    new_path = find_loop(path + [(k, j)])
                    if new_path:
                        return new_path
            return None

        loop = find_loop([(i, j)])

        if not loop:
            print("No loop found!")
            break

        even_cells = loop[1::2]
        theta = min([x[i, j] for i, j in even_cells])

        for idx, (i, j) in enumerate(loop):
            if idx % 2 == 0:
                x[i, j] += theta
            else:
                x[i, j] -= theta

    return x

# Main execution
initial_solution = north_west_corner(supply, demand)
optimal_solution = modi_method(cost, initial_solution)

# Calculate total cost
total_cost = np.sum(optimal_solution * cost)

print("Optimal solution (Allocation Matrix):")
print(pd.DataFrame(optimal_solution))
print("\nTotal Minimum Cost:", total_cost)
