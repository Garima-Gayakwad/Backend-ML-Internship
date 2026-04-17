# counting how many lines are in data.txt
f = open("data.txt", "r")
lines = f.readlines()  # reads each line into a list
f.close()
count = len(lines)
print(f"Total number of lines in data.txt: {count}")
# also printing each line with its number
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.strip()}") 