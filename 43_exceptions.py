# if we input 20 then program will be executed successfully
# thus exit code 0 => success

# if we input asd then program will encounter error
# thus exit code 1 => went wrong


# basic code without exception handling
# age = int(input("Age: "))
# print(age)


# try and except code
try:
    age = int(input("Age: "))
    income = 2000000
    risk = income / age
    print(age)
except ValueError:
    print("LOL!! that's Invalid Value!!")
except ZeroDivisionError:
    print("Opps! Age can't be Zero!")

# note exception is a kind of error which crashes our program
