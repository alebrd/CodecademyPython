# Write your function here
def odd_indices(lst):
    new_lst = []
    for index in lst[1::2]:  # for index in range(1, len(lst), 2): or  [i for i in range(len(lst)) if i % 2 == 1]
        new_lst.append(index)
    return new_lst


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))