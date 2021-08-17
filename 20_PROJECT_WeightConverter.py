# Problem Statement:
# Take Weight as Input from the user.
# Take input weather weight input is in Lbs (input as 'L' or 'l') or Kgs(input as 'K' or 'k')
# convert the weight into the other one from current

weight = input("Weight: ")
format = input("(L)bs or (K)gs: ")

if format.lower() in 'lbs':
    output = str(0.45 * int(weight)) + " Kgs"
elif format.lower() in 'kgs':
    output = str(int(weight) / 0.45) + " Lbs"
else:
    output = "Format is not Proper!"
print(output)
