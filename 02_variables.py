# python is Case Sensitive.

# while declaring variable python
# assign a memory block at certain location and label it as price
# and store a value 13 in it
# before storing this number 13 it will be converted into it's binary representation.
price = 13
# to print price variable
print(price)
# update the price
print('Updated the Price')
price = 30

# till now all the values of price was whole numbers in python it is referred as INTEGERS.
# following rating variable is a floating point number(decimal number in maths)
# in python it is referred as FLOATS.
rating = 4.5
# print price multiple things with a space between them write them as comma seperated in print function.
print(price, rating)

# now we are defining a variable as string
nameOfProduct = "Apple Pie"
print(nameOfProduct, rating, price)

# now we are defining a boolean variable
isAvailable = True
print(nameOfProduct, rating, price, isAvailable)

# note that we can update a variable even if new Datatype is not same as that of Previous
# let's make rating string and then boolean.
rating = '10'
print(rating)
rating = True
print(rating)
