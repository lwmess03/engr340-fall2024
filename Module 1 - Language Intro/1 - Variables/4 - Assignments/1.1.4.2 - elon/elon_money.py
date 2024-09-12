"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 1-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

principal = 33000000000
rate_ten = 3.96
rate_twenty = 4.32
n_ten = 10
n_twenty = 20

A_ten = principal * ((1 + (rate_ten / 100)) ** n_ten)
A_twenty = principal * ((1 + (rate_twenty / 100)) ** n_twenty)

# final answer for 10-year
ten_year_final = A_ten
print("the ten year final is ", ten_year_final);
# final answer for 20-year
twenty_year_final = A_twenty
print("the twenty year final is ", twenty_year_final);