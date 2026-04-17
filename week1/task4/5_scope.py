# scope - global variable and modifying it inside a function
# this is a global variable, can be used anywhere
score = 0
def add_marks(marks):
    global score  
    score += marks
    print(f"Added {marks} marks, total now: {score}")
#marks being added one by one
add_marks(85)
add_marks(90)
add_marks(78)
print("Final score:", score)