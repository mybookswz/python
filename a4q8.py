import numpy as np
from scipy.optimize import linprog

payoff = np.array([
    [-1, -2, 8],
    [7, 5, -1],
    [6, 0, 12]
])

K = abs(payoff.min()) + 1  
payoff_shifted = payoff + K 

c = [1, 1, 1] 
A_ub = -payoff_shifted.T 
b_ub = -np.ones(3) 

res = linprog(c, A_ub=A_ub, b_ub=b_ub, method='highs')

if res.success:
    game_value = 1 / res.fun
    game_value_real = game_value - K 
    strategy = res.x * game_value

    print("Best Strategy for Player A:")
    for i, prob in enumerate(strategy):
        print(f"Play Strategy {i+1} with probability {prob:.4f}")
    print(f"\nValue of the Game = {game_value_real:.4f}")
else:
    print("No solution found.")
