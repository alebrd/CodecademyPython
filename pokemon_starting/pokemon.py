class Pokemon:
    def __init__(self, name, level, type_, health, max_health, is_knocked_out):
        self.name = name
        self.level = level
        self.type_ = type_
        self.health = health
        self.max_health = max_health
        self.is_knocked_out = False

    def lose_health(self, points):
        if type(points) is int:
            self.health -= points
        print('Your {} Pokemon has now {} health.'.format(self.name, self.health))

    def gain_health(self, points):
        if type(points) is int:
            self.health += points
        print('Your {} Pokemon has now {} health.'.format(self.name, self.health))

    def knockedout(self):
        if self.health == 0:
            self.is_knocked_out = True
        print('Your {} has 0 health points so is gone.'.format(self.name))

    def attack(self, another_pokemon, points):
        if type(another_pokemon) is Pokemon:
            if self.type_ == 'Fire':
                if another_pokemon.type_ == 'Grass':
                    points *= 2
                    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Water':
                    points /= 2
                    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Fire':
                    points /= 2
                    another_pokemon.lose_health(points)
            elif self.type_ == 'Grass':
                if another_pokemon.type_ == 'Fire':
                    points /= 2
                    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Water':
                    points *= 2
                    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Grass':
                    points /= 2
                    another_pokemon.lose_health(points)
            elif self.type_ == 'Water':
                if another_pokemon.type_ == 'Grass':
                    points /= 2
                    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Fire':
                    points *= 2
                    another_pokemon.lose_health(points)
                elif another_pokemon.type_ == 'Water':
                    points /= 2
                    another_pokemon.lose_health(points)
        print('Your Pokemon is type: {} and the enemy\'s Pokemon is type: {}.')


class Trainer:
    def __init__(self, name, pokemons, current_pokemon, potions):
        self.name = name
        self.pokemons = pokemons
        self.current_pokemon = current_pokemon
        self.potions = potions
    def attack_other_trainer(self, other_trainer):
        pass
    def heal_current_poke(self):
        pass

