# Write your function here
def over_nine_thousand(lst):
    count_lst = 0
    for num in lst:
        count_lst += num
        if count_lst > 9000:
            break
    return count_lst


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
