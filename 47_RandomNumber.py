# search for python 3 module index
import random
import random as rand

for i in range(3):
    print(rand.random())

for i in range(3):
    print(rand.randint(10, 20))

# given a list of team member pick on as leader randomly
members = ['John', 'Mary', 'Bob', 'Colt', 'Mosh']
members_size = len(members)

print(f'Leader is {members[rand.randint(0, members_size - 1)]}')

# easy way to do this is :
print(f'Leader is {random.choice(members)}')
