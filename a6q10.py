import numpy as np

def european_call_future_binomial(F, K, r, sigma, T, n):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u                        # Down factor
    p = 0.5                          # Risk-neutral probability for futures
    discount = np.exp(-r * dt)       # Discount factor

    # Terminal futures prices
    future_prices = [F * (u**j) * (d**(n - j)) for j in range(n + 1)]
    option_values = [max(f - K, 0) for f in future_prices]  # Payoff at maturity

    # Backward induction
    for i in range(n - 1, -1, -1):
        option_values = [
            discount * (p * option_values[j + 1] + (1 - p) * option_values[j])
            for j in range(i + 1)
        ]

    return option_values[0]

# Inputs for Problem 10
F = 60         # Futures price
K = 60         # Strike price
r = 0.08       # Risk-free interest rate
sigma = 0.30   # Volatility
T = 0.5        # Time to maturity (6 months)
n = 2          # Two steps

# Compute option value
european_call_value = european_call_future_binomial(F, K, r, sigma, T, n)
print("European Call on Futures (2-step):", european_call_value)
