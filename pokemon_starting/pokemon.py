class Pokemon:
    def __init__(self, name, level, type_):   # initializing the Pokemon class
        self.name = name
        self.level = level
        self.type_ = type_
        self.max_health = 80   # just read tha the max health is 80, I might be wrong though.
        self.health = 80
        self.is_knocked_out = False

    def lose_health(self, points):   # the method that is gonna be used to lose health
        if type(points) is int or float:
            self.health -= points
        return 'Your {} Pokemon has now {} health.'.format(self.name, self.health)

    def gain_health(self, points):  # the method that is gonna be used to gain healt
        if type(points) is int or float:
            self.health += points
            if self.health >= self.max_health:
                new_health = self.max_health - 20   # we can never get back to the max health so the max will be 80
                self.health = new_health
        return 'Your {} Pokemon has now {} health.'.format(self.name, self.health)

    def knockedout(self):  # our method to set if a Pokemon is gone or not
        if self.health == 0:
            self.is_knocked_out = True
        return 'Your {} has 0 health points so is gone.'.format(self.name)

    def get_name(self):  # our get_name will be used later in the switch_current method
        return self.name

    def attack(self, another_pokemon):   # our attack method
        points = 25   # I dunno I though is a fair value as start attack points
        if self.is_knocked_out != False:  # when our pokemon is Knocked we are not able to attack
            if type(another_pokemon) is Pokemon:
                if self.type_ == 'Fire':
                    if str(another_pokemon.type_) == 'Grass':
                        points *= 2
                    elif another_pokemon.type_ == 'Water':
                        points /= 2
                    elif another_pokemon.type_ == 'Fire':
                        points /= 2
                    another_pokemon.lose_health(points)
                elif self.type_ == 'Grass':
                    if another_pokemon.type_ == 'Fire':
                        points /= 2
                    elif another_pokemon.type_ == 'Water':
                        points *= 2
                    elif another_pokemon.type_ == 'Grass':
                        points /= 2
                    another_pokemon.lose_health(points)
                elif self.type_ == 'Water':
                    if another_pokemon.type_ == 'Grass':
                        points /= 2
                    elif another_pokemon.type_ == 'Fire':
                        points *= 2
                    elif another_pokemon.type_ == 'Water':
                        points /= 2
                    another_pokemon.lose_health(points)
                return '-Your {} is type: {}.\n' \
                       '-Enemy\'s {} is type: {}.\n' \
                       '-The Enemy\'s Pokemon has lost {} points.\n' \
                       '-Your Pokemon current Health is {}.\n' \
                       '-Enemy\'s Pokemon Health is {}'.format(self.name, self.type_, another_pokemon.name,
                                                               another_pokemon.type_, points,
                                                               self.health, another_pokemon.health)
        else:
            return 'Your Pokemon is Knocked out'


class Trainer:  # our trainer class
    def __init__(self, name, pokemons, current_pokemon, potions):  # defining our trainer class
        self.name = name
        self.pokemons = pokemons  # list of other Pokemons
        self.current_pokemon = current_pokemon  # Pokemon we are using
        self.potions = potions  # potion that heal the current pokemon selected

    def attack_other_trainer(self, other_trainer):  # our attack to the other trainer will be executed using...
        global attack
        if type(other_trainer) is Trainer:
            attack = self.current_pokemon.attack(other_trainer.current_pokemon)   # ...the attack method defined before
        return attack

    def heal_current_pokemon(self):  # healing our pokemon
        if self.potions > 0:  # checking if we did not finish the potions
            current = self.current_pokemon
            self.potions -= 1  # removing one potion
            if type(current) is Pokemon:
                current.gain_health(80)  # using the gain_health method defined before
        return f'Your current Pokemon \'{self.current_pokemon.name}\' has healed.'

    def switch_current(self, name):  # our switching method
        if type(name) is str:
            for switch in self.pokemons:
                if switch.is_knocked_out != False:  # if the pokemon is Knocked we won't be able to switch to it
                    pass
                switch_name = switch.get_name()  # using the get_name defined before for us.
                if str(name) in str(switch_name):
                    self.current_pokemon = switch
            return f'Your current no is {self.current_pokemon.name}.\n' \
                   f'If your Pokemon does not change is probably dead.'
        else:
            return 'Please insert a string'  # in case not a string is inserted


Gabri = Pokemon('Gabri', 10, 'Fire')
Niki = Pokemon('Niki', 10, 'Grass')
Thomas = Pokemon('Thomas', 10, 'Grass')
Gianfro = Pokemon('Gianfro', 10, 'Water')

Alessandro = Trainer('Alessandro', [Gabri], Gabri, 5)
Pezzone = Trainer('Pezzone', [Niki, Thomas, Gianfro], Niki, 5)


