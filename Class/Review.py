class Student:
    def __init__(self, name, year, catch_phrase):
        self.name = name
        self.year = year
        self.grades = []
        self.catch_phrase = catch_phrase

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def get_average(self):  # trying to get the average of the students grades
        count = 0
        for i in self.grades:
            print(i)


roger = Student('Roger van der Weyden', 10, 'aajjs')
sandro = Student('Sandro Botticelli', 12, 'porcodio')
pieter = Student('Pieter Bruegel the Elder', 8, 'You know nothing')


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = int(score)

    def is_passing(self):
        if self.score > self.minimum_passing:
            print('Is passing')


new_grade = Grade(100)
second_grade = Grade(200)
pieter.add_grade(new_grade)
pieter.add_grade(new_grade)
Grade.is_passing(new_grade)
pieter.get_average()
print(pieter.catch_phrase)

# 9.
# Great job! You’ve created two classes and defined their interactions.
# This is object-oriented programming! From here you could:
#
# Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
# Write a Student method get_average() that returns the student’s average score.
# Add an instance variable to Student that is a dictionary called .attendance,
# with dates as keys and booleans as values that indicate whether the student attended school that day.
# Write your own classes to do whatever logic you want!

