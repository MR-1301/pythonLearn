# for loop is used generally to iterate over a collection of data like string or list
string = 'Python'
for item in string:
    print(item)

print("----------------------------------------------")

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

print("----------------------------------------------")

for i in [1, 3, 5, 7, 9]:
    print(i)

print("----------------------------------------------")

# in python we have a range function which return a list based on arguments
# 0 to arg1-1
for itr in range(10):
    print(itr)

print("----------------------------------------------")

# arg1 to arg2-1 increment of 1 every time
for item in range(5, 10):
    print(item)

print("----------------------------------------------")

# arg1 to arg2-1 increment of arg3 every time
for item in range(5, 10, 2):
    print(item)
