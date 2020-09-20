# Write your add_exclamation function here:
def add_exclamation(word):
    count_word_len = len(word)
    print_word = word
    if count_word_len <= 20:
        while len(print_word) <= 20:
            print_word += '!'
        return print_word
    else:
        return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
print(add_exclamation("Ale"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))


# should print Codecademy is the best place to learn


# Write your add_exclamation function here:
def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
