all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    students_in_poetry.append(all_students[-1])
    all_students.pop(-1)


# print(students_in_poetry)

