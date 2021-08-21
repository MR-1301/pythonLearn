# list of names
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# printing the entire list
print(names)
# accessing a particular index
print(names[1])
# we can also use negative index as we do in strings
print(names[-2])
# range of items like we do in strings (right
print(names[2:4])
# note that any of the above operation won't affect the actual list
# we get clone of a list

# modifying the list
names[0] = 'Jon'
print(names)

# all the elements of list need not to be of same type
newList = ['Mahir', 1, False, 6.9]
print(newList)
