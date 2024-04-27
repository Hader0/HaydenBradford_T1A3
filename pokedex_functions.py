import csv

def view_pokedex(pokedex_csv):
    pass


def add_pokemon(pokedex_file):
    pokemon_name = input("Enter the Pokemon name: ") # Create an statement that only accepts 

    number_of_types = input("Does your Pokemon have one or two types? Enter 1 or 2: ")
    
    match number_of_types:
        case "1":
            type1 = input("Please enter the Pokemon type: ")

            with open(pokedex_file, "a") as f:
                writer = csv.writer(f)
                writer.writerow([pokemon_name.capitalize(), type1.capitalize(), "None"])
        case "2":
            type1 = input("Please enter the Pokemon's first type: ")
            type2 = input("Please enter the Pokemon's second type: ")

            with open(pokedex_file, "a") as f:
                writer = csv.writer(f)
                writer.writerow([pokemon_name.capitalize(), type1.capitalize(), type2.capitalize()])
        case _:
            print("Please enter either \"1\" or \"2\"")

def remove_pokemon(pokedex_csv):
    pokemon_name = input("Enter the Pokemon name you would like to remove from the Pokedex: ").capitalize()
    pokemon_list = []

    with open(pokedex_csv, "r") as f:
        reader = csv.reader(f)
        does_exist = False
        for row in reader:
            if (pokemon_name != row[0]):
                pokemon_list.append(row)
            else:
                does_exist = True
    
    if not does_exist:
        print(f"\nYou do not have {pokemon_name.capitalize()} in your Pokedex!\n")
    else:
        
        print(f"\nRemoved {pokemon_name} from your Pokedex!\n")

    with open(pokedex_csv, "w") as f:
        writer = csv.writer(f)
        writer.writerows(pokemon_list)



def view_strengths(pokedex_csv):
    pass

def view_weaknesses(pokedex_csv): 
    pass
