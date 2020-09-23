# These are the emails you will be censoring. The open() function is opening the text file that the emails are containe
# d in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]


def censor_lists_and_words(sentence, badwords, badwords2):  # email_four
    sentence = sentence.lower()
    sentence = sentence.split()
    censored_words = []  # for debugging
    pos_ = []  # index words not listed
    pos_1 = []  # index words not listed too
    new_badwords_list = []
    total_bad_words = badwords + badwords2

    for i in total_bad_words:  # trying to find  the words index before and after the list badwords2
        for word3 in sentence:
            if i in word3:
                pos_.append(sentence.index(word3) - 1)
                pos_1.append(sentence.index(word3) + 1)
                # print(pos_)  # for debugging
                # print(pos_1)  # for debugging

    for i in pos_:
        new_badwords_list.append(sentence[(pos_[0])])

    #################################################################

    for i in total_bad_words:
        for word in sentence:
            if i in word:
                pos = sentence.index(word)
                sentence.remove(word)
                sentence.insert(pos, '*' * len(i))
                censored_words.append(word)

    # for i in new_badwords_list:
    #     for word in sentence:
    #         if i == word:
    #             pos = sentence.index(word)
    #             sentence.remove(word)
    #             sentence.insert(pos, '*' * len(i))
    #             censored_words.append(word)

    print(sentence[(pos_[5])])
    print(pos_[5])
    print(sentence[135]) # for debugging
    print(new_badwords_list)
    sentence_joined = " ".join(sentence).title()
    return sentence_joined


# print(email_four)
print(censor_lists_and_words(email_four, proprietary_terms, negative_words))
