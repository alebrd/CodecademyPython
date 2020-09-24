letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}

letter_to_points[' '] = 0


def score_word(word):
    word_upper = word.upper()
    point_total = 0
    for point in word_upper:
        point_total += letter_to_points.get(point, 0)
    return point_total


print(score_word("brownie"))

brownie_points = 15

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
                   'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}


def update_point_totals(dictionary):
    for key, value in dictionary.items():
        player = key
        words = value
        player_points = 0
        for word in words:
            player_points += score_word(word)
            player_to_points[player] = player_points
    return player_to_points


print(update_point_totals(player_to_words))
play_word_dict = {}


def play_word(dictionary, player, word):
    dictionary[player] = word
    return print("The player {} has chosen the word: '{}'.".format(player, word))


print(play_word(play_word_dict, 'Alessandro', 'Diocane'))



