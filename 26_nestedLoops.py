# generate all the coordinates of form (x,y) where 0<=x<=upperLimitX and 0<=y<=upperLimitY

upper_limit_x = int(input("Enter Upper Limit of x: "))
upper_limit_y = int(input("Enter Upper Limit of y: "))

for x in range(upper_limit_x + 1):
    for y in range(upper_limit_y + 1):
        print(f'({x},{y})')

