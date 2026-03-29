# two sum problem
nums = [2, 7, 11, 15]
target = 9
def two_sum(nums, target):
    prev = {}  # storing numbers we already checked
    for i in range(len(nums)):
        diff = target - nums[i]  # what number do we need?
        if diff in prev:  # if we already saw that number
            return [prev[diff], i]
        prev[nums[i]] = i  # save current number and its index
    return []
result = two_sum(nums, target)
print("answer:", result)  