import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""
middle_1 = len(even_list)//2
middle_2 = (len(even_list)//2) - 1
print(middle_1)
print(middle_2)

middle_1_element = even_list[middle_1]
middle_2_element = even_list[middle_2]

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = (middle_1_element + middle_2_element)/2

# the average of middle elements is
print("The average is: ", middle_average)
