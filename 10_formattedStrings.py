first = 'John'
last = 'Smith'
# print => John [Smith] is a coder
message = first + ' [' + last + '] is a coder'
# better way to do this is: is formatted string
# {} is placeholder and will replace the variable with it's value during execution
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)
