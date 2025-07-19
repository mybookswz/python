import numpy as np
import matplotlib.pyplot as plt

# Strike prices and premiums
K_call = 45
K_put = 40
call_premium = 3
put_premium = 4


S = np.linspace(20, 70, 200)

call_payoff = np.maximum(S - K_call, 0)
put_payoff = np.maximum(K_put - S, 0)
total_premium = call_premium + put_premium
total_profit = call_payoff + put_payoff - total_premium

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(S, total_profit, label='Total Profit', color='blue')
plt.axhline(0, color='black', linestyle=':')
plt.title("Trader's Profit from Long Call + Long Put (Straddle)")
plt.xlabel('Stock Price at Expiry')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.legend()
plt.show()
