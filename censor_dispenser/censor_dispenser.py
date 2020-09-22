# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]


def censor(sentence, badwords):  # email_one
    badwords = badwords.split()
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


# print(censor(email_one, 'learning algorithms'))

def censor_list(sentence, badwords):  # email_two
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
    # print(censored_words)   # for debugging
    sentence_joined = " ".join(sentence).title()
    return sentence_joined


# print(censor_list(email_two, proprietary_terms))

def censor_concerned_tone(sentence, badwords):  # email_three
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

# print(censor_concerned_tone(email_three, negative_words))


# censor for the email_four the terms in the lists above and the words that come before ad after them.


def censor_lists_and_words(sentence, badwords, badwords2):  # email_four
    sentence = sentence.lower()
    sentence = sentence.split()
    censored_words = []  # for debugging
    pos_ = []
    pos_1 = []
    pos__ = []
    pos__2 = []

    for i in badwords2:  # trying to find  the words index before and after the list badwords2
        for word3 in sentence:
            if i in word3:
                pos_.append(sentence.index(word3) - 1)
                pos_1.append(sentence.index(word3) + 1)
                print(pos_)   # for debugging
                print(pos_1)  # for debugging
    #for i in pos_:
      #  for j in sentence:
        #    sentence.remove(j)
        #    sentence.insert(i, '*' * len(j))    # SE RIMUOVI UN INDEX POI TUTTI GLI INDEX SONO SBALLATI. RIPROVA DOMANI
    for i in pos_:
        print(sentence[i])
    for i in badwords:    # trying to find  the words index before and after the list badwords
        for word3 in sentence:
            if i in word3:
                pos__.append(sentence.index(word3) - 1)
                pos__2.append(sentence.index(word3) + 1)
                print(pos__)
                print(pos__2)

    for word in pos_:
        for i in sentence:
            sentence[word].replace(i, '*' * len(i))

    #################################################################

    for i in badwords:
        for word in sentence:
            if i in word:
                pos = sentence.index(word)
                sentence.remove(word)
                sentence.insert(pos, '*' * len(i))
                censored_words.append(word)

    for j in badwords2:
        for words2 in sentence:
            if j in words2:
                pos = sentence.index(words2)
                sentence.remove(words2)
                sentence.insert(pos, '*' * len(j))
                censored_words.append(words2)
    print(censored_words)   # for debugging
    sentence_joined = " ".join(sentence).title()
    return sentence_joined

print(email_four)
print(censor_lists_and_words(email_four, proprietary_terms, negative_words))