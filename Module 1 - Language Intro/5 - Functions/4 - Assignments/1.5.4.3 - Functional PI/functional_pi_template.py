import math


def my_pi(pi):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    a0 = 1
    b0 = 1 / (math.sqrt(2))
    t = 1 / 4
    p = 1

    # perform 10 iterations of this loop
    for i in range(1, 10):
        """
        Step 2: Update each variable based upon the algorithm. Take care to ensure
        the order of operations and dependencies among calculations is respected. You
        may wish to create new "temporary" variables to hold intermediate results
        """

        a = (a0 + b0) / 2
        b = math.sqrt(a0 * b0)
        t = t - (p * (a - a0) ** 2)
        p = 2 * p
        pi = ((a + b) ** 2) / (4 * t)
        a0 = a
        b0 = b

    # change this so an actual value is returned
    return pi




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
