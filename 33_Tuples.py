# tuples are similar to list but we cannot modify them i.e. can't add, remove elements or change order of elements
# tuples are immutable
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(numbers[4])

# can't do following
# numbers[4]=6

# we have only two methods
print(numbers.count(1))
print(numbers.index(3))

# we can use tuple when we don't want any modification later
