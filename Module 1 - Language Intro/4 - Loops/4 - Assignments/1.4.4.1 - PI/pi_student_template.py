import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a0 = 1
b0 = 1/(math.sqrt(2))
t = 1/4
p = 1

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    a = (a0+b0)/ 2
    b = math.sqrt(a0*b0)
    t = t - (p * (a - a0) ** 2)
    p = 2*p
    pi = ((a+b)**2)/(4*t)
    a0 = a
    b0 = b

    initial_1 = None
    initial_2 = None
    initial_3 = None
    initial_4 = None
    initial_5 = None
    initial_6 = None
    initial_7 = None
    greatest_sum = 0
    date_greatest_sum = 0

    for (date, county, state, cases, deaths) in data:
        initial_1 = cases
        if initial_1 != None:
            case_1 = cases - initial_1
            initial_2 = cases
            if initial_2 != None:
                initial_3 = cases
                if initial_3 != None:
                    initial_4 = cases
                    if initial_4 != None:
                        initial_5 = cases
                        if initial_5 != None:
                            initial_6 = cases
                            if initial_6 != None:
                                initial_7 = cases
                                if initial_7 != None:
                                    sum = initial_1 + initial_2 + initial_3 + initial_4 + initial_5 + initial_6 + initial_7
                                    if sum > greatest_sum:
                                        greatest_sum = sum
                                        date_greatest_sum = date
    print(greatest_sum, date_greatest_sum)



    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", pi)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = pi

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
