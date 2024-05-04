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
    pokemon_search = input("Enter the Pokemon you would like to see the Strengths of: ").capitalize()
    other_pokemon = []

    try: # Try block to detect whether the list.csv exists, to prevent the program from crashing
        with open(pokedex_csv, "r") as f:
            reader = csv.reader(f)
            reader.__next__() # Goes to the next row, skipping the first line

            length = 0
            
            for pokemon in reader:
                length+=1

                if (pokemon[0] == pokemon_search): # Checks if the Pokemon matches the Pokemon desired in the list.csv

                    if (pokemon[2] != "None"):
                        type1 = pokemon[1].capitalize()
                        type2 = pokemon[2].capitalize()
                        single = False
                        print(f"\n{pokemon[0]} is available! The types are {type1} & {type2}\n")

                    else:
                        single = True
                        type = pokemon[1].capitalize()
                        print(f"\n{pokemon[0]} is available! The type is {type}\n")

                    types_csv = "types.csv"
                    with open(types_csv, "r") as s:
                        reader = csv.reader(s)
                        reader.__next__() # Goes to the next row, skipping the first line

                        if single == True: # To check if the "type" variable has been assigned a value, if not, the pokemon has more than 1 type and it moves onto else
                            search_type = type + "Strength"
                            for row in reader:
                                if (row[0] == search_type): # Making sure the first value from the CSV row is the same as what the user has searched, in addition to the Strength

                                    sentence = "Strengths are:"
                                    strengths = ""

                                    for i in row[1:]:
                                        strengths += f" {i}, "

                                    print(f"{sentence}" + f"{strengths[:-2]}\n") # Removing the Space and comma at the end of the sentence created by the last loop

                        else: #
                            search_type1 = type1 + "Strength"
                            search_type2 = type2 + "Strength"
                            
                            sentence = "Strengths are:"
                            strengths1 = []
                            strengths2 = []
                            num = 1

                            for row in reader: # Getting the strengths from the first type
                                if (row[0] == search_type1 and num == 1):# Making sure the first value from the CSV row is the same as what the user has searched, in addition to the Strength
                                    if (row[1] == "None"): # To check whether the strength has "None", if it does, then don't include it
                                        pass
                                    else:
                                        strengths1.append(row[1:])
                                        num += 1
                                elif (row[0] == search_type2 and num == 2):
                                    if (row[1] == "None"): # To check whether the strength has "None", if it does, then don't include it
                                        pass
                                    else:
                                        strengths2.append(row[1:])

                            strengthListAll = []
                            for i in strengths1[0]: # Getting all values from Strength1 list and appending to the StrengthList
                                strengthListAll.append(i)
                                # sentence += f" {i},"
                            for i in strengths2[0]: # Getting all values from Strength2 list and appending to the StrengthList
                                strengthListAll.append(i)
                                # sentence += f" {i},"

                            removeDuplicates = set(strengthListAll)

                            for i in removeDuplicates:
                                sentence += f" {i},"

                            print(f"{sentence[:-1]}\n") # Removing the Space and comma at the end of the sentence created by the last loop
                    
                    break # To break the For Loop and stop the incrementing of the 'length' variable
                else:
                    other_pokemon.append(pokemon)

            if (len(other_pokemon) == length): # If 'other_pokemon' and 'length' are the same value, the Pokemon that was searched was not found. If they are not equal, that means the pokemon was found and the incrementation was stopped
                    print(f"\n{pokemon_search} was not found\n")
            # print(other_pokemon)
                    

    except FileNotFoundError:
        print("The Pokedex file doesn't exist")

def view_weaknesses(pokedex_csv): 
    pass
