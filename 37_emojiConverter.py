string = input("Enter a Text: ")
# convert sting stream into a list of words
wordList = string.split(' ')

emoji_converter = {
    ":)": "😊",
    ":(": "😔"
}

ans = ""
for words in wordList:
    ans += emoji_converter.get(words, words) + ' '

print(ans)
