# These are the emails you will be censoring. The open() function is opening the text file that the emails are
# contained in and the .read() method is allowing us to save their contexts to the following variables:
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


#print(censor_concerned_tone(email_three, negative_words))


# censor for the email_four the terms in the lists above and the words that come before ad after them.
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]


def censor_lists_and_words(sentence, badwords, badwords2):  # email_four
    sentence = sentence.lower()
    sentence = sentence.split()
    censored_words = []
    forbidden_words = badwords + badwords2
    for i in forbidden_words:
        for word in sentence:
            if i in word:

                for x in punctuation:  # Censoring the forbidden words list
                    word.strip(x)
                pos = sentence.index(word)
                sentence.remove(word)
                sentence.insert(pos, 'X' * len(i))
                censored_words.append(word)
    input_text_words = []
    for x in sentence:
        x1 = x.split("\n")
        for word in x1:
            input_text_words.append(word)
    for i in range(0, len(input_text_words)):
        checked_word = input_text_words[i].lower()
        for x in punctuation:
            checked_word = checked_word.strip(x)
        if checked_word in forbidden_words:

            word_before = input_text_words[i - 1]    # Censoring the word before the targeted word
            for x in punctuation:
                word_before = word_before.strip(x)
            censored_word_before = ""
            for x in range(0, len(word_before)):
                censored_word_before = censored_word_before + "X"
            input_text_words[i - 1] = input_text_words[i - 1].replace(word_before, censored_word_before)

            word_after = input_text_words[i + 1]     # Censoring the word after the targeted word
            for x in punctuation:
                word_after = word_after.strip(x)
            censored_word_after = ""
            for x in range(0, len(word_after)):
                censored_word_after = censored_word_after + "X"
            input_text_words[i + 1] = input_text_words[i + 1].replace(word_after, censored_word_after)

    print(censored_words)  # debugging purpose
    sentence_joined = " ".join(sentence).title()
    return sentence_joined


print(censor_lists_and_words(email_four, proprietary_terms, negative_words))
