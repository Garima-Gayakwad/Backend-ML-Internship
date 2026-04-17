# *args - function that takes any number of values
def sum_numbers(*args):
    total = 0
    for n in args:  # looping through all numbers passed
        total += n
    return total
# testing with different number of arguments
print("Sum of 1,2,3:", sum_numbers(1, 2, 3))
print("Sum of 10,20:", sum_numbers(10, 20))
print("Sum of 5,10,15,20,25:", sum_numbers(5, 10, 15, 20, 25))
#adding more marks
print("total marks:", sum_numbers(85, 90, 78, 92, 88))