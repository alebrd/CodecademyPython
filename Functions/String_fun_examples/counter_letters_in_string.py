letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Write your unique_english_letters function here:
def unique_english_letters(word):
    counter = 0
    counter_lst = []
    for letter in word:
        if letter not in counter_lst:
            counter_lst.append(letter)
            counter += 1
    return counter


# Uncomment these function calls to test your function:

print(unique_english_letters("mississippi"))
# should print 4

print(unique_english_letters("Apple"))
# should print 4
