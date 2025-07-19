import numpy as np
import matplotlib.pyplot as plt

K = 150 
premium = 5
St = np.linspace(100,200,100)

#Long call 
payoff = np.maximum(St-K,0)
profit = payoff - premium
plt.plot(St,payoff,label='Payoff')
plt.plot(St,profit,label='Profit',linestyle='--')
plt.xlabel('Stock price')
plt.ylabel('Payoff/profit')
plt.legend()
plt.title('Long call ')
plt.grid(True)
plt.axhline(0,color='black',linestyle=':')
plt.show()

#Short call
payoff = -np.maximum(St-K,0)
profit = payoff + premium
plt.plot(St,payoff,label='Payoff')
plt.plot(St,profit,label='Profit',linestyle='--')
plt.xlabel('Stock price')
plt.ylabel('Payoff/profit')
plt.legend()
plt.grid(True)
plt.title('Short call ')
plt.axhline(0,color='black',linestyle=':')
plt.show()

#Long put
payoff = np.maximum(K-St,0)
profit = payoff - premium
plt.plot(St,payoff,label='Payoff')
plt.plot(St,profit,label='Profit',linestyle='--')
plt.xlabel('Stock price')
plt.ylabel('Payoff/profit')
plt.legend()
plt.grid(True)
plt.title('Long put ')
plt.axhline(0,color='black',linestyle=':')
plt.show()

#Short put
payoff = -np.maximum(K-St,0)
profit = payoff + premium
plt.plot(St,payoff,label='Payoff')
plt.plot(St,profit,label='Profit',linestyle='--')
plt.xlabel('Stock price')
plt.ylabel('Payoff/profit')
plt.legend()
plt.grid(True)
plt.title('Short put')
plt.axhline(0,color='black',linestyle=':')
plt.show()
