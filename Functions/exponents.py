# Write your function here
def exponents(bases, power):
    new_list = []
    for base in bases:
        for pow in power:
            new_list.append(base ** pow)
    return new_list


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

