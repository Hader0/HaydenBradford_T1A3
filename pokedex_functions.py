import csv

def view_pokedex(pokedex_csv):
    pass

def add_pokemon(pokedex_file):
    pokemon_name = input("Enter the Pokemon name: ") # Takes in a name, whether it be an official Pokemon or a made-up Pokemon

    number_of_types = input("Does your Pokemon have one or two types? Enter 1 or 2: ")

    allTypes = ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']
    
    match number_of_types:
        case "1":
            type1 = input("Please enter the Pokemon type: ").capitalize() # Takes the pokemon type in
            if allTypes.count(type1) > 0 and type1 != "": # Checks if the type matches one of the correct types in the allTypes list
                with open(pokedex_file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([pokemon_name.capitalize(), type1.capitalize(), "None"]) # Writes the name and type to the next line in list.csv
                print(f"\n{pokemon_name.capitalize()} added to the Pokedex!")
            else:
                print("\nPokemon not added - Incorrect Type. Please choose one of the available below:\n")
                print("Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon, Dark, Steel, Fairy")
                
            print("\n") # To space the menu from the line above once the input has been accepted

        case "2":
            type1 = input("Please enter the Pokemon's first type: ").capitalize()
            wrong = 0
            if allTypes.count(type1) > 0 and type1 != "":
                pass
            else:
                wrong += 1
            type2 = input("Please enter the Pokemon's second type: ").capitalize()
            if allTypes.count(type2) > 0 and type2 != "":
                pass
            else:
                wrong += 1

            print("\n") # To space the menu from the line above once the input has been accepted

            if wrong > 0: # If the wrong value is more than 0, one of the types are incorrect
                print("\nPokemon not added - Incorrect Type/s. Please choose one of the available below:\n")
                print("Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon, Dark, Steel, Fairy\n")
            
            elif type1 == type2: # Checks if both types are the same value
                print("Pokemon cannot have 2 of the same types. Please either choose 1 type or choose another from below:\n")
                print("Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon, Dark, Steel, Fairy\n")
            else: # If all above is correct, the pokemon is finally added to the pokedex
                with open(pokedex_file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([pokemon_name.capitalize(), type1.capitalize(), type2.capitalize()]) # Writes the name and both types to the next line in the list.csv
                print(f"\n{pokemon_name.capitalize()} added to the Pokedex!\n")

        case _: # If either 1 or 2 wasn't entered
            print("\nPlease enter either \"1\" or \"2\"\n")

def remove_pokemon(pokedex_csv):
    pokemon_name = input("Enter the Pokemon name you would like to remove from the Pokedex: ").capitalize()
    pokemon_list = []

    with open(pokedex_csv, "r") as f: # Opening the list.csv
        reader = csv.reader(f)
        does_exist = False # A value to be used when the pokemon cannot be found in the file
        for row in reader:
            if (pokemon_name != row[0]): # Checking if the pokemon name is the same as that pokemon row
                pokemon_list.append(row)
            else:
                does_exist = True 
    
    if not does_exist: # Once the pokemon is not found, the value being True, ouputs the below message
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

                            for i in strengths2[0]: # Getting all values from Strength2 list and appending to the StrengthList
                                strengthListAll.append(i)

                            removeDuplicates = set(strengthListAll)

                            for i in removeDuplicates:
                                sentence += f" {i},"

                            print(f"{sentence[:-1]}\n") # Removing the Space and comma at the end of the sentence created by the last loop
                    
                    break # To break the For Loop and stop the incrementing of the 'length' variable
                
                else:
                    other_pokemon.append(pokemon)

            if (len(other_pokemon) == length): # If 'other_pokemon' and 'length' are the same value, the Pokemon that was searched was not found. If they are not equal, that means the pokemon was found and the incrementation was stopped
                    print(f"\n{pokemon_search} was not found\n")

    except FileNotFoundError:
        print("The Pokedex file doesn't exist")

def view_weaknesses(pokedex_csv): 
    pokemon_search = input("Enter the Pokemon you would like to see the Weaknesses of: ").capitalize()
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
                            search_type = type + "Weakness"
                            for row in reader:
                                if (row[0] == search_type): # Making sure the first value from the CSV row is the same as what the user has searched, in addition to the Weakness

                                    sentence = "Weaknesses are:"
                                    weaknesses = ""

                                    for i in row[1:]:
                                        weaknesses += f" {i}, "

                                    print(f"{sentence}" + f"{weaknesses[:-2]}\n") # Removing the Space and comma at the end of the sentence created by the last loop

                        else: #
                            search_type1 = type1 + "Weakness"
                            search_type2 = type2 + "Weakness"
                            
                            sentence = "Weaknesses are:"
                            weaknesses1 = []
                            weaknesses2 = []
                            num = 1

                            for row in reader: # Getting the weaknesses from the first type
                                if (row[0] == search_type1 and num == 1):# Making sure the first value from the CSV row is the same as what the user has searched, in addition to the weakness
                                    if (row[1] == "None"): # To check whether the weakness has "None", if it does, then don't include it
                                        pass

                                    else:
                                        weaknesses1.append(row[1:])
                                        num += 1

                                elif (row[0] == search_type2 and num == 2):
                                    if (row[1] == "None"): # To check whether the weakness has "None", if it does, then don't include it
                                        pass

                                    else:
                                        weaknesses2.append(row[1:])

                            weaknessListAll = []
                            for i in weaknesses1[0]: # Getting all values from weakness1 list and appending to the weaknessList
                                weaknessListAll.append(i)

                            for i in weaknesses2[0]: # Getting all values from weakness2 list and appending to the weaknessList
                                weaknessListAll.append(i)

                            removeDuplicates = set(weaknessListAll)

                            for i in removeDuplicates:
                                sentence += f" {i},"

                            print(f"{sentence[:-1]}\n") # Removing the Space and comma at the end of the sentence created by the last loop
                    
                    break # To break the For Loop and stop the incrementing of the 'length' variable
                
                else:
                    other_pokemon.append(pokemon)

            if (len(other_pokemon) == length): # If 'other_pokemon' and 'length' are the same value, the Pokemon that was searched was not found. If they are not equal, that means the pokemon was found and the incrementation was stopped
                    print(f"\n{pokemon_search} was not found\n")

    except FileNotFoundError:
        print("The Pokedex file doesn't exist")
