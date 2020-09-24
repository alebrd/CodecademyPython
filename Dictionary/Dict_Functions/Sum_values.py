# Write your sum_values function here:
def sum_values(my_dictionary):
    count = 0
    for i in my_dictionary.values():
        count += i
    return count


# Uncomment these function calls to test your sum_values function: SUM THE VALUES
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))


# should print 6


# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
    count = 0
    for i in my_dictionary.keys():
        if i % 2 == 0:
            count += my_dictionary[i]
    return count


# Uncomment these function calls to test your  function:   IF THE KEY IS EVEN, THEN SUM THE VALUES
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))


# should print 6


# Write your add_ten function here:   # ADD TEN TO EACH KEY
def add_ten(my_dictionary):
    for key, value in my_dictionary.items():
        key_value = key
        nums = value
        my_dictionary[key_value] = nums + 10
    return my_dictionary


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))


# should print {10:11, 100:12, 1000:13}


# Write your values_that_are_keys function here: VALUES THAT ARE KEYS, CHECK IF VALUE IN KEY AND RETURN IT
def values_that_are_keys(my_dictionary):
    the_list = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            the_list.append(value)
    return the_list


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))


# should print ["a"]


# Write your max_key function here:   RETURN THE KEY WHICH HAS THE HIGHER NUMBER IN THE VALUES
def max_key(my_dictionary):
    largest_key = ''
    largest_value = -10000
    for i in my_dictionary:
        if my_dictionary[i] > largest_value:
            largest_value = my_dictionary[i]
            largest_key = i
    return largest_key


print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# prints 1
print(max_key({"a": 100, "b": 10, "c": 1000}))


# Write your word_length_dictionary function here: NEW DICTIONARY, WORDS AS KEYS AND VALUES AS LEN(WORDS)
def word_length_dictionary(words):
    the_dict = {}
    for i in words:
        the_dict[i] = len(i)
    return the_dict


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))


# should print {"a": 1, "": 0}


# Write your frequency_dictionary function here:  counting how many times a word repeat in the list.
def frequency_dictionary(words):
    the_dict = {}
    for c in words:
        if c not in the_dict:
            the_dict[c] = 1
        else:
            the_dict[c] += 1
    return the_dict


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))


# should print {0:5}


# Write your unique_values function here:
def unique_values(my_dictionary):
    unique = []
    for i in my_dictionary.values():
        if i not in unique:
            unique.append(i)
    return len(unique)


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1
