def every_three_nums(start):
    if start > 100:
        empty = []
        return empty
    else:
        new_lst = list(range(start, 101, 3))
        return new_lst


# Uncomment the line below when your function is done
print(every_three_nums(91))