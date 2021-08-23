# take a phone number as a input and will give a word output
# Eg.
# Phone: 1234
# output: One Two Three Four

dictionary = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone = input("Phone: ")

ans = ""
for num in phone:
    ans += dictionary.get(num, "!") + ' '

print(ans)
