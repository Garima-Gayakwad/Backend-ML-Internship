# lambda - short anonymous function
# using lambda with map() to square all numbers in a list
nums = [1, 2, 3, 4, 5]
print("Original list:", nums)
# lambda x: x**2 means -> take x, return x squared
squared = list(map(lambda x: x ** 2, nums))
print("Squared list:", squared)
#trying with my own numbers
My_nums = [3, 6, 9, 12]
result = list(map(lambda x: x ** 2, My_nums))
print("My squared list:", result)