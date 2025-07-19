import numpy as np

payments = np.array([460, 235, 640, 370, 330, 250]) 
interest_rate_annual = 0.045                   
compounding_periods_per_year = 4              

effective_annual_rate = (1 + interest_rate_annual / compounding_periods_per_year) ** compounding_periods_per_year - 1

years = np.arange(1, 7) 
present_values = payments / (1 + effective_annual_rate) ** years

total_present_value = present_values.sum()

print("Present Values for Each Year:")
for year, payment, pv in zip(years, payments, present_values):
    print(f"  Year {year}: Payment = {payment}, Present Value = {pv:.2f}")
print("\nTotal Present Value of All Payments: ${:.2f}".format(total_present_value))
