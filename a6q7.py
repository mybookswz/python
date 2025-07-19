import numpy as np

S = 19         
K = 20    
r = 0.03     
T = 4/12       
C = 1        
   
P = C + K * np.exp(-r * T) - S

print(f"Price of the 4-month European put: ${P:.2f}")
