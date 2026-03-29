f = open("data.txt", "w")
f.write("Line 1: My name is Garima\n")
f.write("Line 2: I am learning Python Backend\n")
f.write("Line 3: Python is interesting\n")
f.write("Line 4: I study in SPIT\n")
f.write("Line 5: This is my internship task\n")
f.close()  # always close the file after writing
print("data.txt created and 5 lines written!")