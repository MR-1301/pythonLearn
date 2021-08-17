# conversion from one type to another data type
birth_year = input("What is Your birthyear? ");
# without type conversion we have 2021 - '2001' which is invalid.
print(type(birth_year))
print(type(int(birth_year)))

age = 2021 - int(birth_year)
print(age)
