import random
import string
# function to generate a random password
# uses letters, numbers and special characters
def generate_password(length):
    # combining all character types
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ""
    for i in range(length):
        pwd += random.choice(chars)  # picking one random char each time
    return pwd