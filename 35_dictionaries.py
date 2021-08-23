# bunch of key value pairs

# each key should be unique
# datatype of key can be strings or numbers
# even both strings and numbers are allowed to be used simultaneously in one dictionary
# datatype of value can be anything
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True,
}

# accessing the dictionary using a key
# will return value associated with name key
print(customer["name"])

# but using above method with the key that doesn't exist will give error
# so it's better to use .get()
# if not found then .get() function will return Nothing
# if found it will return the corresponding key!!
print(customer.get("Name"))
print(customer.get("name"))

# we can also supply a default value along with get function
# this default value is printed when key is not found

print(customer.get("Name", "Name Field doesn't exist"))

# updating the dictionary
customer["name"] = "Jack Smith"
print(customer)

# if the key doesn't exist then
# it will create a new key with same name and then will assign the value
customer["birthdate"] = "1 Jan 1999"
print(customer)

