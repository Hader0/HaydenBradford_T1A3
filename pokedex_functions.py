def view_pokedex(pokedex_file):


def add_pokemon(pokedex_file):
    pokemon_name = input("Enter the Pokemon name: ") # Create an statement that only accepts 

    number_of_types = input("Does your Pokemon have one or two types? Enter 1 or 2: ")
    
    match number_of_types:
        case "1":
            type1 = input("Please enter the Pokemon type: ")
        case "2":
            type1 = input("Please enter the Pokemon's first type: ")
            type2 = input("Please enter the Pokemon's second type: ")
        case _:
            print("Please enter either \"1\" or \"2\"")

def remove_pokemon(pokedex_file):


def view_strengths(pokedex_file):


def view_weaknesses(pokedex_file):
