import numpy as np

face_value = 100
coupon_rate = 0.08
coupon = face_value * coupon_rate 
years = np.array([1, 2, 3, 4, 5])
y = 0.11 
y_new = 0.108 


cash_flows = np.array([coupon] * 4 + [coupon + face_value])
discount_factors = np.exp(-y * years)
price = np.sum(cash_flows * discount_factors)
print(f"(a) Bond Price: ${price:.2f}")

weighted_times = years * (cash_flows * discount_factors)
duration = np.sum(weighted_times) / price
print(f"(b) Duration: {duration:.4f} years")

delta_y = -0.002 
price_change = -duration * price * delta_y
new_price_estimate = price + price_change
print(f"(c) Estimated Price with 0.2% drop in yield: ${new_price_estimate:.2f}")

discount_factors_new = np.exp(-y_new * years)
price_new = np.sum(cash_flows * discount_factors_new)
print(f"(d) Actual Price at 10.8% yield: ${price_new:.2f}")

difference = abs(price_new - new_price_estimate)
print(f"Difference between (c) and (d): ${difference:.4f}")
