course = 'Python for Beginners'

# total number of char in string
# len is general purpose function
size = len(course)
print(size)

# as upper and similar function are available only for string or more specifically
# string class it's called as method of string class
# note that this method does not change or modify our original string
# it crates a new string and returns it
upper_course = course.upper()
print(course)
print(upper_course)
print(course.lower())

# to find the first occurrence of a particular character in string
# it is case sensitive and returns index
# return first occurrence's index if multiple present
# returns -1 if no occurrence found
print(course.find('P'))
print(course.find('o'))
print(course.find('z'))

# we can also pass the sequence of characters
# return the index where passed sequence is starting in actual string
print(course.find('Beginners'))

# to replace a character or substring of char by some other char or substring
new_course = course.replace('Beginners', 'Pros')
print(new_course)

# check a existance of char or substring present in acutal string
print('for' in course)
print('python' in course)

# note every above method is case sensitive
