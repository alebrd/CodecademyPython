# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    word1_string = word1.replace(word1[0], word2[0])
    word2_string = word2.replace(word2[0], word1[0])
    new_string = word1_string + ' ' + word2_string
    return new_string


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
