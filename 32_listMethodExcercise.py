# Write an program to remove duplicated in a list

numbers = [5, 4, 6, 6, 1, 1, 5, 6, 4, 3, 1, 2, 2, 1]
i = 0

while i < len(numbers):
    if numbers.count(numbers[i])>1:
        numbers.remove(numbers[i])
    else:
        i += 1;

print(numbers)
