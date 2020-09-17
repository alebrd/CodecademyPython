# Write your function here
def add_greetings(names):
    greeting = []
    for i in names:
        i = 'Hello, ' + i
        greeting.append(i)
    return greeting


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))