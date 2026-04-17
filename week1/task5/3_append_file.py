# adding a new line without deleting old content
# "a" mode means append - adds to end of file
f = open("data.txt", "a")
f.write("Line 6: I added this line later\n")
f.close()
print("New line added to data.txt!")
# reading to confirm it was added
f = open("data.txt", "r")
print(f.read())
f.close()