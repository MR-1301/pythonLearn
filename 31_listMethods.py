# note that this all methods changes our acutal list

numbers = [5, 2, 1, 7, 4]

# add a number at the end
numbers.append(13)
print(numbers)

# add a number at the particular index of the list
numbers.insert(0, 20)
print(numbers)
numbers.insert(2, 1)
print(numbers)

# remove a particular number
numbers.remove(1)
print(numbers)
# note that it will remove first occurance of the passed argument


# note that we can't do a clone by clone_number=numbers because it will just assign two name to
# same list and making any changes in any of them will be reflected in other one
clone_number = numbers[:]
# clearing all the elements from clone
clone_number.clear()
print(clone_number)
print(numbers)

# remove the list item in the list
numbers.pop()
print(numbers)

numbers.append(1)
print(numbers)
# find a first occurance of the any given number
# and will give error if doesn't exist
print(numbers.index(1))
# print(numbers.index(50)) #will give error

# so the best way to find index is to check first that
# x = int(input("Enter a NUmber You want to find: "))
x = 55
if x in numbers:
    print(numbers.index(x))
else:
    print("Number not Found!!")

# count total occurance of a number in list
print(numbers.count(1))

# sorting Methods
ascending = numbers[:]
descending = numbers[:]

# ascending
# Meaning of None is python:
# sort method return nothing so when we print the method sort applied on numbers it will print None
print(ascending.sort())
print(ascending)

# descending
descending.sort()
# reverses the list
descending.reverse()
print(descending)

# create a copy of list
copy_of_list = numbers[:]  # method-1
copy_of_list = numbers.copy()  # method-2
print(copy_of_list)
