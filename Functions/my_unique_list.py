myUniqueList = []
myLeftovers = []


def new_addition(new):
    if new not in myUniqueList:
        myUniqueList.append(new)
        return True
    else:
        myLeftovers.append(new)
        return False


new_addition(4)
new_addition("Khloe")
new_addition("Khloe")
new_addition("ale")
new_addition("ale")
new_addition("fra")
print(myUniqueList)
print(myLeftovers)
