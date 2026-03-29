# longest substring without repeating characters
# for example in "abcabcbb", longest is "abc" = length 3
s = "abcabcbb"
def longest_sub(s):
    seen = {}    # store last position of each character
    left = 0     # left side of our window
    max_len = 0  # tracking the longest we found

    for right in range(len(s)):
        ch = s[right]
        # if we saw this character before, move left pointer
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right  # update last seen position
        # check if current window is the longest
        max_len = max(max_len, right - left + 1)
    return max_len
ans = longest_sub(s)
print("Longest substring length:", ans) 
#testing with another string
print("For 'garima' answer is:", longest_sub("garima")) 