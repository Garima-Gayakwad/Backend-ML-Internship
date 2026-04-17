# opening and reading the file we created
# "r" mode means read
f = open("data.txt", "r")
content = f.read()  # reads everything
f.close()
print("Contents of data.txt:")
print(content)