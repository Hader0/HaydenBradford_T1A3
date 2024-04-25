import os.path
from pokedex_functions import view_pokedex, add_pokemon, remove_pokemon, view_strengths, view_weaknesses

print("Welcome to your Pokedex!\n")

def pokedex_menu(): # The main menu the user can see when initially running the application
    print("1. Enter 1 to view your Pokedex")
    print("2. Enter 2 to add a Pokemon to your Pokedex")
    print("3. Enter 3 to remove a Pokemon from your Pokedex")
    print("4. Enter 4 to see the strengths of a Pokemon")
    print("5. Enter 5 to see the weaknesses of a Pokemon")
    print("6. Enter 6 to exit\n")

    user_choice = input("Enter your selection: ") # Accepts the user input
    print(" ")
    return user_choice

pokedex_csv = "list.csv"
if (not os.path.isfile(pokedex_csv)): # Checking if the file exists - if the file doesn't exist, it will create one
    print("Creating file as it doesn't exist")
    # Creating the file
    pokedex_file = open(pokedex_csv, "w")
    # Insert headiungs into the file
    pokedex_file.write("name,type1,type2\n")
    # Close the file
    pokedex_file.close()

choice = ""

while choice != "5": # Keeps the application running until "choice" is changed to 5

    choice = pokedex_menu()

    if (choice == "1"):
        view_pokedex(pokedex_file)
    elif (choice == "2"):
        add_pokemon(pokedex_file)
    elif (choice == "3"):
        remove_pokemon(pokedex_file)
    elif (choice == "4"):
        view_strengths(pokedex_file)
    elif (choice == "5"):
        view_weaknesses(pokedex_file)
    elif (choice == "6"):
        choice = "6"
    else:
        print("That is not an option. Please try again!")

print("Thanks for using the TODO list application!")