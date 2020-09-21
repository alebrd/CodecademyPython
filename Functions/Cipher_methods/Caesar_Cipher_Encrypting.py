
message = 'xuo lyixqb! pxyi yi q ikfuh seeb syfxuh, jxqdai veh ixemydw cu! pxqj ubiu oek wej?'

def encrypt(string, swift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    translated_message = ''
    for letter in string:
        if letter not in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + swift) % 26]
        else:
            translated_message += letter
    return translated_message


# print(encrypt(message, 10))

message2 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

print(encrypt(message2, 14))
