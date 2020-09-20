alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"


def crypt(string, swift):
    translated_message = ''
    for letter in string:
        if letter not in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - swift) % 26]
        else:
            translated_message += letter
    return translated_message


# print(crypt(message, 10))

message_for_v = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"
translated_message = ""
for letter in message_for_v:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value - 10) % 26]
    else:
        translated_message += letter
print(translated_message)
