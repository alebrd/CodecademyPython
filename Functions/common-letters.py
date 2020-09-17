def contains(big_string, little_string):
    for i in big_string:
        if little_string in big_string:
            return True
        else:
            return False


def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if letter in string_two and letter not in common:
            common.append(letter)
        else:
            continue
    return common
