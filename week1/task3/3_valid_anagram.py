# valid anagram problem
s = "anagram"
t = "nagaram"
def check_anagram(s, t):
    # if we sort both strings, anagrams will look exactly the same
    if sorted(s) == sorted(t):
        return True
    return False
print(s, "and", t, "are anagram?", check_anagram(s, t))  # True
# another test
print(check_anagram("rat", "car"))  # False, different letters