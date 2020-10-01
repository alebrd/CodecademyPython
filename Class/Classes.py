class Bonsai:
    def __init__(self, type_, color, vase_color):
        self.type_ = type_
        self.color = color
        self.vase_color = vase_color


fico = Bonsai('Ficus', 'Green & Brown', 'White')

print(fico.color)


class person:
    name = 'Agnieszka'
    height = 170
    weight = 55
    eyes_color = 'Blue'

    def __init__(self, name, height, weight, eyes_color):
        self.name = name
        self.height = height
        self.weight = weight
        self.eyes_color = eyes_color

Aga = person

print(Aga.name)

fra = person('Fra', 150, 60, 'black')


print(fra.name)

class Tv:
    def __init__(self, brand, model, size):
        self.brand = brand
        self.model = model
        self.size = size


agaTV = Tv('Sony', 'Bravia', 55)

print(agaTV.brand)

