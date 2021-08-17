# we can use both '..' and ".." for strings but if we want one of them
# in side the string then we should use the other one.

# following both of the styles are valid and we can't use single quotes in firt
# one and awe can't use double quotes in second one.
course = "Mosh's Python for Beginners"
msg = 'Pam said "Go to Paris Jim" excitedly'
print(course)
print(msg)

# we can also use triple quotes of larger strings having multiple lines
email = '''
Hey Pam,

This is a mail to infrom you that your
profile has been shortlisted for interview. 

Congrats and Regards,
Jim.

'''

print(email)

course = 'Python for Beginners'
# accessing element at partcular index. (0 indexed)
print(course[1])
# we can use negative index which access the element from end -1 means last index
size = len(course)
print(course[-1])
print(course[-2])
print(course[-size])

# extract multiple characters using : syntax
# returns a substring from 0th index to 2nd index excluding the 3rd index(i.e. the right number)
print(course[0:3])
# default value on left of : is 0 and right of : is size of string
print(course[4:])
print(course[:6])

# to clone a string
another_string = course[:]
print(another_string)
