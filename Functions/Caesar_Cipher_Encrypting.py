alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. ' \
          'muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'


def encrypt(string, swift):
    translated_message = ''
    for letter in string:
        if letter not in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + swift) % 26]
        else:
            translated_message += letter
    return translated_message


print(encrypt(message, 10))
