

nums = [4, 8, 15, 16, 23, 42]
double_nums = [num * 2 for num in nums]
print(double_nums)

nums = range(11)
# squares = [num * num for num in nums]
squares = [num ** 2 for num in nums]

print(squares)

nums = [4, 8, 15, 16, 23, 42]

add_ten = [num + 10 for num in nums]

nums = [4, 8, 15, 16, 23, 42]

divide_by_two = [num // 2 for num in nums]
print(divide_by_two)

nums = [4, 8, 15, 16, 23, 42]
parity = [num % 2 for num in nums]
print(parity)

names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ['Hello, ' + name for name in names]
print(greetings)

names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]
print(first_character)

names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(i) for i in names]
print(lengths)

booleans = [True, False, True]
opposite = [not i for i in booleans]
print(opposite)

names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [i == 'Jerry' for i in names]
print(is_Jerry)

nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [i * j for (i, j) in nested_lists]
print(product)

nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [ x > y for (x, y) in nested_lists]
print(greater_than)

nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [x for (x, y) in nested_lists]
print(first_only)

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [x + y for (x, y) in zip(a,b)]
print(sums)

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [y / x for (x, y) in zip(a, b)]
print(quotients)

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

locations = [capital + ', ' + country for (capital, country) in zip(capitals, countries)]

print(locations)

names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

users = ['Name: ' + name + ', Age: ' + str(age) for (name, age) in zip(names, ages)]
print(users)

a = [30, 42, 10]
b = [15, 16, 17]

greater_than = [x > y for (x, y) in zip(a, b)]
print(greater_than)

