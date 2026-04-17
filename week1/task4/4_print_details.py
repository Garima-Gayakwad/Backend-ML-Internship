# **kwargs - prints all key value pairs
def print_details(**kwargs):
    print("Details:")
    for key, value in kwargs.items():  # looping through all key-value pairs
        print(f"  {key}: {value}")
    print("   ")
# calling with different details
print_details(name="Garima", age=20, city="Mumbai", course="CS")
print_details(name="ABC", hobby="cricket", college="SPIT")