highlighted_poems = "Afterimages:Audre Lorde:1997,  " \
                    "The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   " \
                    "Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, " \
                    "" \
                    "The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, " \
                    "Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, " \
                    "Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)  # first print no changes
print()

highlighted_poems_list = highlighted_poems.split(',')

print(highlighted_poems_list)  # second print; we splitted the string making it a list with various string inside

highlighted_poems_stripped = []  # creating an empty list for the stripping of the previous splitted list

for clean in highlighted_poems_list:  # iterating through each string to remove the white spaces
    highlighted_poems_stripped.append(clean.strip())  # appending the result of the stripping to the new list

print()

print(highlighted_poems_stripped)  # third print; the string inside the list have been cleaned by the extra spaces

highlighted_poems_details = []   # creating an empty list for the splitting of the previous stripped list

for clean in highlighted_poems_stripped:   # iterating through each cleaned string in the list and
    highlighted_poems_details.append(clean.split(':'))   # making each sub-string a new sub-list

print()
print(highlighted_poems_details)   # fourth print; the list now has many sub-lists inside of it cleaned.

titles = []                        # RESUME: WE FIRST SPLIT TO CREATE A LIST OF SUB-STRING.
poets = []                         # THEN WE STRIP TO CLEAN THE DIRTY THINGS LIKE: EXTRA SPACES OR WEIRED CHARACTER
dates = []                         # THEN WE SPLIT AGAIN TO CREATE SUB-LISTS INSIDE THE LIST

for i in highlighted_poems_details:           # THEN WE CREATE EMPTY LISTS
    titles.append(i[0])                       # THEN WE HAVE A LIST WITH SUB-LISTS AND WE CAN ITERATE IN EACH ONE
    poets.append(i[1])                        # THEN WE APPEND EACH i with the Index position inside the sub-list
    dates.append(i[2])

# for i in range(0, len(highlighted_poems_details)):
#    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
print()
for i in range(0, len(highlighted_poems_details)):
    print(f'The poem {titles[i]} was published by {poets[i]} in {dates[i]}')
