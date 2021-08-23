def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print("Welcome aboard!!")


print("Start")
# function as reusable chunk of code
# takes up default value ""

# positional arguments
greet_user("John", "Smith")
# non-positional arguments (using keyWord Arguments)
greet_user(last_name="Smith", first_name="John")
# note that keyword arguments must occur after positional arguments
# greet_user(first_name="John","Smith") # error
greet_user("John", last_name="Smith")
print("Finish")

