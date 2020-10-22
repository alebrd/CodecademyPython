mylambda = lambda x: x[0] + x[-1]
print(mylambda('Ciao'))

mylambda_if_else = lambda x: x[0] + x[-1] if x >= 2 else x
print(mylambda('Ciao'))

add_two = lambda my_input: my_input + 2

is_substring = lambda my_string: my_string in "This is the master string"

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'


mylambda2 = lambda age: 'Welcome to BattleCity!' if age >= 13 else 'You must be over 13'
print(mylambda2(14))

get_last_name = lambda name: name.split()[-1]
print(get_last_name('Jane Doe'))