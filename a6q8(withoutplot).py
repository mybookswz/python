import numpy as np
from scipy.stats import norm

def bs_call(S, K, r, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def bs_put(S, K, r, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

S = 32        
sigma = 0.30     
r = 0.05     

T1 = 0.5
K1 = 25
K2 = 30
call_low = bs_call(S, K1, r, T1, sigma)
call_high = bs_call(S, K2, r, T1, sigma)
cost_bull_spread = call_low - call_high
print(f"(a) Cost of Bull Spread (Calls): ${cost_bull_spread:.2f}")


put_low = bs_put(S, K1, r, T1, sigma)
put_high = bs_put(S, K2, r, T1, sigma)
cost_bear_spread = put_high - put_low
print(f"(b) Cost of Bear Spread (Puts): ${cost_bear_spread:.2f}")


T2 = 1.0
K3 = 25
K4 = 30
K5 = 35
call1 = bs_call(S, K3, r, T2, sigma)
call2 = bs_call(S, K4, r, T2, sigma)
call3 = bs_call(S, K5, r, T2, sigma)
cost_butterfly = call1 - 2 * call2 + call3
print(f"(c) Cost of Butterfly Spread (Calls): ${cost_butterfly:.2f}")
