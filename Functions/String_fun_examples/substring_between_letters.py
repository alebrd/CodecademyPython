# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    start_index = word.find(start)
    end_index = word.find(end)
    if start_index and end_index != -1:
        substring = word[start_index + 1:end_index]
        return substring
    else:
        return word


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
