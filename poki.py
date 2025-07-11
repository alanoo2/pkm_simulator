import random as rdm
import time
import sys

band = False

def print_words(text):  # to write on screen with delay
    for word in text.split():
        sys.stdout.write(word + ' ')
        sys.stdout.flush()
        time.sleep(0.7)
    print()  # new line at the end

# movements class
class movement:
    def __init__(self, name, power, types):
        self.name = name
        self.power = power
        self.types = types    

    def __str__(self):
        return f"{self.name} (Power: {self.power})"

# pokemons class
class pokemon:
    nivel = 1

    def __init__(self, name, types, max_life, curr_life):
        self.name = name
        self.types = types
        self.max_life = max_life
        self.curr_life = max_life
        self.moves = []    

    def __str__(self):
        return f"{self.name} ({self.types})"

    def check_pkm(self):
        print("Pokemon data: ")
        print(f"Level: {self.nivel}")
        print(f"Name: {self.name}")
        print(f"Types: {self.types}")
        print(f"Max life: {self.max_life}")
        print(f"Current life: {self.curr_life}")

    def heal_pkm(self): # heal pokemons life
        if self.curr_life == self.max_life:
            print('Your Pokemon is READY TO FIGHT!')
        else:
            print_words(". . . puf")
            self.curr_life = self.max_life
            time.sleep(0.7)
            print("COMPLETELY HEALED")
    
    def add_movement(self, movement):   # add movements to pokemons
        if len(self.moves) < 4:
            self.moves.append(movement)  # Add movement object directly
        else:
            print(f"{self.name} already has 4 movements.")

    def show_moves(self):   # show movements
        print(f"{self.name}'s moves:")
        for i, move in enumerate(self.moves):
            print(f"{i+1} - {move}")

    def atack(opponent):
        opponent.curr_life = opponent.curr_life - (opponent.curr_life*0.4)

# moves availables
Tackle = movement("Tackle",35,"Normal")
Ember = movement("Ember",40,"Fire")

# pokes availables
Bulbasaur = pokemon("Bulbasaur","Plant-Poison",10,10)
Bulbasaur.add_movement(Tackle)
Squirtle =  pokemon("Squirtle","Water",10,10)
Squirtle.add_movement(Tackle)
Charmander = pokemon("Charmander","Fire",10,10)
Charmander.add_movement(Tackle)


pokes = [Bulbasaur,Squirtle,Charmander]
def battle(poke):   # function to simulate battles
    opponent = rdm.choice(pokes)
    print_words(f"Your opponent is {opponent} ")

    while True:
        print_words("Choose an attack")
        poke.show_moves()
        opc = int(input( ))

       # you attack
        move = poke.moves[opc - 1]  # get the move object
        damage = opponent.max_life * (0.01 * move.power)
        opponent.curr_life -= damage
        print_words(f"Opponents current life is {opponent.curr_life}")
        lolo = str( input( ) )

        # ends battle if opponent's life is less than 0        
        if opponent.curr_life < 0:
            print(f"The winner is {poke}")
            return
       
       # opponent attacks
        opponent_atack = rdm.choice(opponent.moves)
        print_words(f"Opponent {opponent} chooses {opponent_atack} ")
        damage = poke.max_life * (0.01 * opponent_atack.power)
        poke.curr_life -= damage
        print_words(f"{poke} current life is {poke.curr_life}")
        lolo = str( input( ) )


        if poke.curr_life < 0:
            print(f"The winner is {poke}")
            return
        elif opponent.curr_life < 0:
            print(f"The winner is {opponent}")
            return
# end simulate battles

select_init = int(input("Select your initial \n1. Bulbasaur\n2. Squirtle\n3. Charmander\n -> "))
while not band:
    match select_init:  # selector of first pokemon
        case 1:
            selected = Bulbasaur; band = True
        case 2:
            selected = Squirtle; band = True
        case 3:
            selected = Charmander; band = True
        case _:
            print('again')        

while band:
    opc = int(input("Would you like to check your pokemon stats, heal him or battle?\n 1. Check stats\n2. Show moves\n3. Heal him\n4. BATTLE!\n -> ") )
    match opc:  # options for pokemons
        case 1: 
            selected.check_pkm()
        case 2:
            selected.show_moves()
        case 3:
            selected.heal_pkm()
        case 4:
            battle(selected)
        case _: 
            print("FUCK U"); band = False
        