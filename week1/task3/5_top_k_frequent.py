# top k frequent elements
# find which numbers appear the most
nums = [1, 1, 1, 2, 2, 3]
k = 2  # we want top 2 most frequent
def top_k(nums, k):
    freq = {}  # count how many times each number appears
    for n in nums:
        if n in freq:
            freq[n] += 1  # already seen, increase count
        else:
            freq[n] = 1   # first time seeing it
    # sort by frequency, highest first
    res = sorted(freq, key=freq.get, reverse=True)
    return res[:k]  # return only top k
ans = top_k(nums, k)
print("Top", k, "frequent numbers:", ans) 