# HaydenBradford_T1A3

View Strengths:
Turn values from list into string: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.

## Styling Guide
- Camel_case used for Classes
- Comments capitilised with one space between # and comment

The code was written referencing the PEP 8 Style Guide for Python using the Black Code Style and formatter as it is PEP8 compliant.

The styles followed include:

- Lower case variables with underscores (example_variable)
- 79 character line limit
- 4 Space indentation
- Blank lines to seperate functions
- Imports seperated by lines and grouped
- Use of double quotes consistently


## Features

#### View Pokedex
This function was by far the easiest in the project. It opens the list.csv file and row by row, collects the Name and Types of each Pokemon and prints as, for example: 

- Pikachu: Electric
- Zapdos: Flying, Electric

At the end of function, after outputting all available Pokemon and their types, it also prints how many pokemon they have collected, with the amount increasing with each Pokemon looped over.

![View Pokedex Function](/docs/viewpokedex.png)

#### Add Pokemon
First of all, Pokemon have certain types such as Fire, Water, Ground, Fighting. I included all official types into a list. When the function runs, the Pokemon name input from the user can be anything, as you can even add your own made up Pokemon. Then the user is asked if the Pokemon has 1 or 2 types, for which need to be different from each other and match a type in the "official" list, otherwise an error message appears and the user needs to start over. Once the types have been accepted, the Pokemon name and type/s are added to the list.csv file. For example:

- Pikachi,lightning,None
- Zapdos,flying,electric

If the Pokemon only has 1 type, the third value will be "None".

Then the user is present with a message saying: "Pikachu has been added to the Pokedex!"

![View Pokedex Function](/docs/addpokemon.png)
![View Pokedex Function](/docs/addpokemon2.png)

#### Remove Pokemon
For the user to remove a Pokemon from the Pokedex, the functions starts off by asking for the Pokemon name. In the beginning, there is an empty list. When the list.csv file opens and the lines are looped through, each Pokemon row that does not match with the specified input, it is then added to the list. If there is no Pokemon with the same name, an error message appears. If the Pokemon does exist, it is not added to the new list, then that list overwrites the list.csv file with all the Pokemon that did not match the name and the user is presented with a message saying: "Removed Pikachu from your Pokedex!"

![View Pokedex Function](/docs/removepokemon.png)

#### View Strengths/Weaknesses
The View Strengths and View Weaknesses functions are both essentially the same as they perform the same job, except they both have different values, for example: strength_list versus weakness_list. Since a Pokemon can have 1 or 2 values, a Pokemon with only 1 value with have a row a row such as below:

Pikachu,lightning,None

The functions start off asking the user for the Pokemon they would like to see the strength/weakness of, as well as having an empty list that will have all Pokemon that don't match the name specifed by the user appended to. 

Once the Pokemon name is inputted, the list.csv file is opened and each row is looped through to find the matching Pokemon. For each loop, there is a value that increments by 1. If the pokemon the user searched for doesn't exist in the file, it is decided by the amount of disqualifying pokemon in the list created at the beginning being of equal amount to the value that increased for each loop. Then the user is presented with a message saying: "Pikachu was not found!". If the Pokemon is found, the list will be shorter than the incremented value. Once the Pokemon name matches with the user input and decided whether the Pokemon has a value of "None" instead of a second type, 