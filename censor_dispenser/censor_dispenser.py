# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor_words(email, word1, word2):
    email_lower = email.lower()
    word1_lower = word1.lower()
    word2_lower = word2.lower()
    email_splitted = email_lower.split()
    for i in email_splitted:
        if i == word1_lower:
            email_splitted.remove(i)
    for i in email_splitted:
        if i == word2_lower:
            email_splitted.remove(i)
    email_joined = ' '.join(email_splitted).title()
    return email_joined


def censor(sentence, badwords):
    bad_words = badwords.split()
    sentence = sentence.lower
    sentence = sentence.split()
    for i in bad_words:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))

    return " ".join(sentence).title()


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm",
                     "her", "herself"]


def censor_list(sentence, badwords):
    sentence = sentence.lower()
    sentence = sentence.split()
    censored_words = []  # for debugging
    for i in badwords:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))
                censored_words.append(words)
    print(censored_words)  # for debugging
    sentence_joined = " ".join(sentence).title()
    return sentence_joined


# print(email_two)

# print(censor_list(email_two, proprietary_terms))


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control",
                  "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]
print(email_three)
print()
print(censor_list(email_three, negative_words))


def censor_concerned_tone(sentence, badwords):
    sentence = sentence.lower()
    sentence = sentence.split()
    censored_words = []
    for i in badwords:
        for words in sentence:
            if i in words:
                censored_words.append(words)
                if i != censored_words[-1]:
                    pos = sentence.index(words)
                    sentence.remove(words)
                    sentence.insert(pos, '*' * len(i))
    print(censored_words)  # for debugging
    sentence_joined = " ".join(sentence).title()
    return sentence_joined


print(censor_concerned_tone(email_three, negative_words))
