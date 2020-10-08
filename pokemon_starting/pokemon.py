class Pokemon:
    def __init__(self, name, level, type_):              # initializing the Pokemon class
        self.name = name
        self.level = level
        self.type_ = type_
        self.max_health = 80                             # just read tha the max health is 80, I might be wrong though.
        self.health = 80
        self.is_knocked_out = self.knockedout()

    def lose_health(self, points):                       # the method that is gonna be used to lose health
        if type(points) is int or float:
            self.health -= points
        if self.health <= 0:
            self.health = 0
            self.knockedout()
        return 'Your {} Pokemon has now {} health.'.format(self.name, self.health)

    def gain_health(self, points):                       # the method that is gonna be used to gain health
        gained_health = self.health                      # local variable to find out how many points we gained
        if type(points) is int or float:
            self.health += points
            if self.health >= self.max_health:
                new_health = self.max_health - 20        # we can never get back to the max health so the max will be 80
                self.health = new_health
        gained_health = self.health - gained_health
        return 'Your {} Pokemon gained {} health.'.format(self.name, gained_health)

    def knockedout(self):                                # our method to set if a Pokemon is gone or not
        if self.health > 0:
            self.is_knocked_out = False
            return f'The Pokemon named {self.name} is not Knocked out yet.'
        if self.health <= 0:
            self.is_knocked_out = True
            return f'The Pokemon named {self.name} is Knocked out.'

    def attack(self, another_pokemon):                   # our attack method
        points = 25                                      # I dunno I think is a fair value as start attack points
        if self.health > 0:                              # when our pokemon is Knocked we are not able to attack
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
                   '-Enemy\'s Pokemon Health is {}.'.format(self.name, self.type_, another_pokemon.name,
                                                           another_pokemon.type_, points,
                                                           self.health, another_pokemon.health)
        else:
            return f'The Pokemon {self.name} is Knocked out so it can\'t attack.'

    def get_name(self):                                 # our get_name will be used later in the switch_current method
        return self.name

    def get_health(self):  # our method to get the health
        return f'Your {self.name} Pokemon has {self.health} health points.'


class Trainer:                                           # our trainer class
    def __init__(self, name, pokemons, current_pokemon, potions):  # defining our trainer class
        self.name = name
        self.pokemons = pokemons                         # list of other Pokemons
        self.current_pokemon = current_pokemon           # Pokemon we are using
        self.potions = potions                           # potion that heal the current pokemon selected

    def attack_other_trainer(self, other_trainer):       # our attack to the other trainer will be executed using...
        global attack
        if type(other_trainer) is Trainer:
            attack = self.current_pokemon.attack(other_trainer.current_pokemon)   # ...the attack method defined before
        return attack

    def heal_current_pokemon(self):                      # healing our pokemon
        if self.potions > 0:                             # checking if we did not finish the potions
            current = self.current_pokemon
            self.potions -= 1                            # removing one potion
            if type(current) is Pokemon:
                current.gain_health(80)                  # using the gain_health method defined before
        return f'Your current Pokemon {self.current_pokemon.name} has healed ' \
               f'to the max 60 points.'                  # can't heal to the max so I decide 80 - 20 points

    def switch_current(self, name):                      # our switching method
        global switch
        if type(name) is str:
            for switch in self.pokemons:
                switch_name = switch.get_name()          # using the get_name defined before for us.
                if str(name) in str(switch_name):
                    if switch.health <= 0:               # if the pokemon is Knocked we won't be able to switch to it
                        self.current_pokemon = self.current_pokemon
                        break
                    self.current_pokemon = switch
            return f'Your current Pokemon selected is now {self.current_pokemon.name}.\n' \
                   f'If your Pokemon does not switch is probably dead or does not exist.'
        else:
            return 'Please insert a string name.'          # in case not a string is inserted

    def get_current_name(self):
        return f'Your current Pokemon selected name is {self.current_pokemon.name}.'

    def get_potions(self):
        return f'You\'ve got {self.potions} potions left.'


Charizard = Pokemon('Charizard', 10, 'Fire')                                  # CREATING OUR POKEMONS OBJECTS
Blaziken = Pokemon('Blaziken', 10, 'Fire')
Infernape = Pokemon('Infernape', 10, 'Fire')


Bulbasaur = Pokemon('Bulbasaur', 10, 'Grass')
Pumpkaboo = Pokemon('Pumpkaboo', 10, 'Grass')
Celebi = Pokemon('Celebi', 10, 'Grass')

Blastoise = Pokemon('Blastoise', 10, 'Water')
Gyarados = Pokemon('Gyarados', 10, 'Water')
Keyogre = Pokemon('Keyogre', 10, 'Water')


Red = Trainer('Red', [Charizard, Bulbasaur, Blastoise], Charizard, 5)        # CREATING OUR TRAINER OBJECTS
Blue = Trainer('Blue', [Blaziken, Pumpkaboo, Gyarados], Pumpkaboo, 5)
Drake = Trainer('Drake', [Infernape, Celebi, Keyogre], Keyogre, 5)


print(Red.attack_other_trainer(Drake))    # testing TRAINER ATTACK
print()
print(Bulbasaur.attack(Keyogre))          # {POKEMON ATTACK} to Keyogre to knock it out
print(Bulbasaur.attack(Keyogre))
print()

print(Drake.switch_current('Infernape'))  # SWITCHING POKEMON TEST to Infernape

print(Drake.switch_current('Keyogre'))    # trying to SWITCH to a Knocked out Pokemon, it won't switch cause is Gone

print(Drake.get_current_name())           # printing the GET_NAME of the current pokemon after trying to switch it

print()

print(Infernape.knockedout())             # Testing our KNOCKEDOUT method
print(Keyogre.knockedout())
print(Keyogre.get_health())               # testing GET_HEALTH method

print()

print(Keyogre.gain_health(10))            # GAIN_HEALTH from 0 to 10 health points
print(Keyogre.get_health())               # GET_HEALTH shows 10 points back

print()

print(Drake.switch_current('Keyogre'))    # testing SWITCHING BACK again to Keyogre which isn't knocked out anymore
print(Keyogre.get_health())               # showing GET_HEALTH before the heal_current_pokemon method is used
print(Drake.heal_current_pokemon())       # testing the HEAL_CURRENT_POKE method
print(Keyogre.get_health())               # showing the GET_HEALTH after the method
print(Keyogre.gain_health(100))           # when it GET_HEALTH is max to 60 points

print()

print(Bulbasaur.get_health())             # testing the methods on another Pokemon, GET_HEALTH
print(Bulbasaur.lose_health(100))         # health points cannot go below 0 health, LOSE_HEALTH
print(Bulbasaur.get_health())             # the health points can't go below the 0, GET_HEALTH
print(Bulbasaur.gain_health(100))         # once is healed it can't get more than 60 points, GAIN_HEALTH
print(Bulbasaur.get_health())             # test the points, GET_HEALTH

print()

print(Drake.get_potions())                # prints how may potions left, GET_POTIONS
print(Charizard.lose_health(100))         # test LOSE_HEALTH on Charizard
print(Red.attack_other_trainer(Blue))     # testing if it can attack when is knocked out, ATTACK_OTHER_TRAINER
print(Charizard.attack(Bulbasaur))        # testing if it can attack when is knocked out, ATTACK OTHER POKEMON

