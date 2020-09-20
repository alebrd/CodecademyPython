# Write your x_length_words function here:
def x_length_words(sentence, x):
    sentence_split = sentence.split()
    for length in sentence_split:
        if x <= len(length):
            return True
        else:
            return False


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
