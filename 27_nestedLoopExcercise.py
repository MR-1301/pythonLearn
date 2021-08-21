# draw the below given shape using nested loops
# xxxxx
# xx
# xxxxx
# xx
# xx

for i in range(2):
    print('x' * 5)
    for j in range(i + 1):
        print('x' * 2)
