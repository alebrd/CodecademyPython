coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl " \
                "tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."


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

# The easiest way to break this code is to simply brute force though all of the possible shifts.
# We'll only need to try 25 different shifts, so it's not computationally expensive. Then we can
# look through all of the outputs and look for the one that in english, and we've decoded our message!


for i in range(1,26):
    print("offset: " + str(i))
    print("\t " + encrypt(coded_message, i) + "\n")

print(encrypt(coded_message, 7))

