import numpy as np
import matplotlib.pyplot as plt

K1 = 25
K2 = 30
K3 = 25
K4 = 30
K5 = 35

call_K1 = 4   
call_K2 = 2  
put_K1 = 1     
put_K2 = 3  
call_K3 = 4    
call_K4 = 2.5   
call_K5 = 1    


S = np.linspace(10, 50, 400)


bull_payoff = np.maximum(S - K1, 0) - np.maximum(S - K2, 0)
bull_cost = call_K1 - call_K2
bull_profit = bull_payoff - bull_cost


bear_payoff = np.maximum(K2 - S, 0) - np.maximum(K1 - S, 0)
bear_cost = put_K2 - put_K1
bear_profit = bear_payoff - bear_cost


butterfly_payoff = (
    np.maximum(S - K3, 0)
    - 2 * np.maximum(S - K4, 0)
    + np.maximum(S - K5, 0)
)
butterfly_cost = call_K3 - 2 * call_K4 + call_K5
butterfly_profit = butterfly_payoff - butterfly_cost

plt.figure(figsize=(7, 4))
plt.plot(S, bull_profit, label='Bull Spread (Profit)', color='green')
plt.axhline(0, color='black', linestyle='--')
plt.title('Bull Spread using Calls')
plt.xlabel('Stock Price at Maturity')
plt.ylabel('Net Profit')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(7, 4))
plt.plot(S, bear_profit, label='Bear Spread (Profit)', color='red')
plt.axhline(0, color='black', linestyle='--')
plt.title('Bear Spread using Puts')
plt.xlabel('Stock Price at Maturity')
plt.ylabel('Net Profit')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(7, 4))
plt.plot(S, butterfly_profit, label='Butterfly Spread (Profit)', color='blue')
plt.axhline(0, color='black', linestyle='--')
plt.title('Butterfly Spread using Calls')
plt.xlabel('Stock Price at Maturity')
plt.ylabel('Net Profit')
plt.legend()
plt.grid(True)
plt.show()
