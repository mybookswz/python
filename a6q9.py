import numpy as np
import scipy.stats as si

S = 30      
K = 29          
r = 0.05       
T = 4 / 12     
sigma = 0.25     

d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
#(a)
call_price_euro = S * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2)
#(b)
call_price_american = call_price_euro  
#(c)
put_price_euro = K * np.exp(-r * T) * si.norm.cdf(-d2) - S * si.norm.cdf(-d1)
#(d)
lhs = call_price_euro + K * np.exp(-r * T)
rhs = put_price_euro + S
put_call_parity_holds = np.isclose(lhs, rhs)


print("European Call Option Price:   ${:.2f}".format(call_price_euro))
print("American Call Option Price:   ${:.2f}".format(call_price_american))
print("European Put Option Price:    ${:.2f}".format(put_price_euro))

print("Left Side (C + K*e^(-rT)):    {:.5f}".format(lhs))
print("Right Side (P + S):           {:.5f}".format(rhs))
print("Does Put-Call Parity Hold?:   {}".format("Yes" if put_call_parity_holds else "No"))
