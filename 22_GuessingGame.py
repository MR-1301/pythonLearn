# Set a secret number from 1 to 9
# User Enters a number from 1 to 9 randomly
# User has three chance to Guess
print("Solution-1")
# Solution-1

secret = 8
counter = 3

while counter > 0:
    guess = int(input("Guess: "))
    if guess == secret:
        print("You Win!!")
        break  # break statement helps us to terminate the loop
    counter -= 1

if counter == 0:
    print("You Lost!!")

# Alternative way to use else block of while

print("Solution-2")
# Solution-2
# Note that if while does not face any break statement in between
# i.e. executed completely then else part will come into picture.

counter = 3
while counter > 0:
    guess = int(input("Guess: "))
    if guess == secret:
        print("You Win!!")
        break  # break statement helps us to terminate the loop
    counter -= 1
else:
    print("You Lost!!")
