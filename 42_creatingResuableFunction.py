# convert sting stream into a list of words

def emoji_converter(string):
    word_list = string.split(' ')

    dictionary = {
        ":)": "😊",
        ":(": "😔"
    }

    ans = ""
    for words in word_list:
        ans += dictionary.get(words, words) + ' '

    return ans


print(emoji_converter(input("> ")))
