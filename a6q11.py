import numpy as np

def american_put_stock_binomial(S, K, r, q, sigma, T, n):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))              # Up factor
    d = 1 / u                                     # Down factor
    p = (np.exp((r - q) * dt) - d) / (u - d)      # Risk-neutral probability
    discount = np.exp(-r * dt)                    # Discount factor

    # Terminal stock prices
    stock_prices = [S * (u**j) * (d**(n - j)) for j in range(n + 1)]
    option_values = [max(K - s, 0) for s in stock_prices]  # Payoff at maturity

    # Backward induction with early exercise
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            stock_price = S * (u**j) * (d**(i - j))  # Stock at node
            hold = discount * (p * option_values[j + 1] + (1 - p) * option_values[j])
            exercise = max(K - stock_price, 0)
            option_values[j] = max(hold, exercise)  # American = max(hold, exercise)

    return option_values[0]

# Inputs for Problem 11
S = 484         # Stock index level
K = 480         # Strike price
r = 0.10        # Risk-free rate
q = 0.03        # Dividend yield
sigma = 0.25    # Volatility
T = 2 / 12      # Time to maturity (2 months = 1/6 year)
n = 4           # 4 half-month steps

# Compute option value
american_put_value = american_put_stock_binomial(S, K, r, q, sigma, T, n)
print("American Put on Stock (4-step):", american_put_value)
