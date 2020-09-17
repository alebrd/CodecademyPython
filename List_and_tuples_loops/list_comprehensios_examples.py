heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [can for can in heights if can > 161]

# print(can_ride_coaster)


celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp * (9 / 5) + 32 for temp in celsius]

# print(fahrenheit)


single_digits = [num for num in range(10)]

squares = []

for singl in single_digits:
    print(singl)
    sqa = singl ** 2
    squares.append(sqa)
# print(squares)

cubes = [third ** 3 for third in single_digits]

# print(cubes)
