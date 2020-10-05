class Pokemon:
    def __init__(self, name, level, type_, health):
        self.name = name
        self.level = level
        self.type_ = type_
        self.health = health
        self.max_health = 100
        self.is_knocked_out = False

    def lose_health(self, points):
        if type(points) is int:
            self.health -= points
        return 'Your {} Pokemon has now {} health.'.format(self.name, self.health)

    def gain_health(self, points):
        if type(points) is int:
            self.health += points
            if self.health > self.max_health:
                self.health = self.max_health
        return 'Your {} Pokemon has now {} health.'.format(self.name, self.health)

    def knockedout(self):
        if self.health == 0:
            self.is_knocked_out = True
        return 'Your {} has 0 health points so is gone.'.format(self.name)

    def attack(self, another_pokemon):
        points = 25
        if type(another_pokemon) is Pokemon:
            if self.type_ == 'Fire':
                if str(another_pokemon.type_) == 'Grass':
                    points *= 2
                #    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Water':
                    points /= 2
                #    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Fire':
                    points /= 2
                another_pokemon.lose_health(points)
            elif self.type_ == 'Grass':
                if another_pokemon.type_ == 'Fire':
                    points /= 2
                #    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Water':
                    points *= 2
                #    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Grass':
                    points /= 2
                another_pokemon.lose_health(points)
            elif self.type_ == 'Water':
                if another_pokemon.type_ == 'Grass':
                    points /= 2
                #    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Fire':
                    points *= 2
                #    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Water':
                    points /= 2
                another_pokemon.lose_health(points)
        print('-Your {} is type: {}.\n'
              '-Enemy\'s {} is type: {}.\n'
              '-The Enemy\'s Pokemon has lost {} points.\n'
              '-Your Pokemon current Health is {}.\n'
              '-Enemy\'s Pokemon Health is {}'.format(self.name, self.type_, another_pokemon.name, another_pokemon.type_, points,
                                                      self.health, another_pokemon.health))


class Trainer:
    def __init__(self, name, pokemons, current_pokemon, potions):
        self.name = name
        self.pokemons = pokemons  # Must be a list of Pokemon Class.
        self.current_pokemon = current_pokemon  # Pokemon selected
        self.potions = potions  # potion that heal the current pokemon selected
        self.current_pokemon_name = self.current_pokemon.name

    def __repr__(self):
        return str(self.current_pokemon)

    def attack_other_trainer(self, other_trainer):
        if type(other_trainer) is Trainer:
            their_pokemon = other_trainer.current_pokemon
            current = self.current_pokemon
            if type(current) is Pokemon:
                current.attack(their_pokemon)

    def heal_current_pokemon(self):
        if self.potions > 0:
            current = self.current_pokemon
            self.potions -= 1
            if type(current) is Pokemon:
                current.gain_health(100)
        return f'Your current Pokemon \'{self.current_pokemon}\' has healed'

    def switch_current(self):
        pass


Gabri = Pokemon('Gabri', 10, 'Fire', 50)
Niki = Pokemon('Niki', 10, 'Grass', 100)

#Gabri.attack(Niki)

Alessandro = Trainer('Alessandro', [Gabri], Gabri, 5)
Pezzone = Trainer('Pezzone', [Niki], Niki, 5)

Pezzone.attack_other_trainer(Alessandro)

print(Pezzone.current_pokemon_name)



