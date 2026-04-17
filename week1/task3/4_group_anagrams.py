# group anagrams problem
# putting words that are anagrams of each other into same group
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams(words):
    d = {}  # dictionary to store groups
    for w in words:
        key = tuple(sorted(w))  # sorted word is the key
        if key not in d:
            d[key] = []  # create new group
        d[key].append(w)  # add word to its group
    return list(d.values())
groups = group_anagrams(words)
print("Grouped anagrams:")
for g in groups:
    print(g)