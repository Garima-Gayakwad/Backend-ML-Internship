# contains duplicate problem
# checking if any number appears more than once in the list
nums = [1, 2, 3, 1]  # 1 appears twice so answer is True
def contains_dup(nums):
    s = set(nums)  # set removes duplicates automatically
    # if lengths are different, there was a duplicate
    if len(s) != len(nums):
        return True
    return False
print("Does list have duplicate?", contains_dup(nums))
# testing with no duplicates
nums2 = [1, 2, 3, 4]
print("Does list have duplicate?", contains_dup(nums2))  # False