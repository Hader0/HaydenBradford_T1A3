# HaydenBradford_T1A3

## Q3: Reference Sources

All code created was influenced by previous lessons and the project we made from the last lesson. I did have a link from a website I thought I would use but I never ended up using that in my code as I came up with a more suitable way.

## Q4: GitHub Repository Link

[Click Here to Visit Repository](https://github.com/Hader0/HaydenBradford_T1A3)

## Q5: Styling Guide and Conventions
- Camel_case used for Classes
- Comments capitilised with one space between # and comment

The code was written referencing the PEP 8 Style Guide for Python using the Black Code Style and formatter as it is PEP8 compliant.

The styles followed include:

- Lower case variables with underscores (example_variable)
- 4 Space indentation
- Blank lines to seperate functions
- Imports seperated by lines and grouped
- Use of double quotes consistently


## Q6: Walkthrough and Logic of Features

#### View Pokedex
This function was by far the easiest in the project. It opens the list.csv file and row by row, collects the Name and Types of each Pokemon and prints as, for example: 

- Pikachu: Electric
- Zapdos: Flying, Electric

At the end of function, after outputting all available Pokemon and their types, it also prints how many pokemon they have collected, with the amount increasing with each Pokemon looped over.

![View Pokedex Function](/docs/images/viewpokedex.png)

#### Add Pokemon
First of all, Pokemon have certain types such as Fire, Water, Ground, Fighting. I included all official types into a list. When the function runs, the Pokemon name input from the user can be anything, as you can even add your own made up Pokemon. Then the user is asked if the Pokemon has 1 or 2 types, for which need to be different from each other and match a type in the "official" list, otherwise an error message appears and the user needs to start over. Once the types have been accepted, the Pokemon name and type/s are added to the list.csv file. For example:

- Pikachi,lightning,None
- Zapdos,flying,electric

If the Pokemon only has 1 type, the third value will be "None".

Then the user is present with a message saying: "Pikachu has been added to the Pokedex!"

![Add Pokemon Function](/docs/images/addpokemon.png)
![Add Pokemon Function - 2](/docs/images/addpokemon2.png)

#### Remove Pokemon
For the user to remove a Pokemon from the Pokedex, the functions starts off by asking for the Pokemon name. In the beginning, there is an empty list. When the list.csv file opens and the lines are looped through, each Pokemon row that does not match with the specified input, it is then added to the list. If there is no Pokemon with the same name, an error message appears. If the Pokemon does exist, it is not added to the new list, then that list overwrites the list.csv file with all the Pokemon that did not match the name and the user is presented with a message saying: "Removed Pikachu from your Pokedex!"

![Remove Pokemon Function](/docs/images/removepokemon.png)

#### View Strengths/Weaknesses
The View Strengths and View Weaknesses functions are both essentially the same as they perform the same job, except they both have different variables, for example: strength_list versus weakness_list. Since a Pokemon can have 1 or 2 types, a Pokemon with only 1 type will have a row such as below:

Pikachu,lightning,None

The functions start off asking the user for the Pokemon they would like to see the strength/weakness of, as well as having an empty list that will have all Pokemon that don't match the name specifed by the user appended to. 

Once the Pokemon name is inputted, a try block detects whether the list.csv file exists, if not, the file is created after displaying the following messages:

- "The Pokedex file doesn't exist"
- "Creating file as it doesn't exist"
- ""list.csv" file created!"

![Try/Except File Creation Error Code](/docs/images/filecreated.png)

Once the Try/Except block is finished, the list.csv file is then opened and each row is looped through to find the matching Pokemon. For each loop, there is a variable that increments by 1. If the pokemon the user searched for doesn't exist in the file, it is decided by the amount of disqualifying pokemon in the list created at the beginning being of equal amount to the variable that increased for each loop. Then the user is presented with a message saying: "Pikachu was not found!". If the Pokemon is found, the list will be shorter than the incremented variable. Once the Pokemon name matches with the user input and decided whether the Pokemon has does not value of "None" instead of a second type, both types are then capitalised and the following is printed to the user:

"Zapdos is available! The types are Electric and Flying

![Detecting Whether The Pokemon Has More Than One Type](/docs/images/onetype1.png)

If the Pokemon's second type is "None, therefore a pokemon having just one type, the following is printed to the user:

"Pikachi is available! The type is Electric"

![Detecting Whether The Pokemon Has More Than One Type](/docs/images/twotype1.png)

Once the function has an understanding of how many types the Pokemon has, a variable is set to the types.csv file, the purpose of which has a list of all types that shows the strengths and weaknesses for. For example, the electric weaknesses and strengths is formatted as below:

![Electric Pokemon Strength And Weaknesses](/docs/images/electrictypes.png)

That file is then opened by the CSV library and if the Pokemon had a single type, a variable is created with the Electric type and the string "Strength" or "Weakness". For example, I will be using strength. The variable will then be "ElectricStrength". The file is looped through rows looking for "ElectricStrength" in the first value of the row. Once that ElectricStrength variable matches that first row's value, a for loop is created and each strength for the electric type is appended to a string sentence which the following is outputted:

"Strengths are: Water, Ground, Rock"

![Code Block For Finding And Outputting Pokemon Strength/Weakness That Have 1 Type](/docs/images/onetype2.png)

If the Pokemon has 2 types, then the else statement is used. For this example, I will use Zapdos since it has two types of Flying and Electric and we will be outputting the strengths of each on one string. For each type, a strengths_1 and strengths_2 list is created for the strengths that will be found and added to. Then a "num" variable is created with the value of "1". 

![Else Statement For a Pokemon With 2 Types](/docs/images/twotype2.png)

After those lists and the variable is created, a for loop is created to loop through each row finding the first types strength. This is done if the row's first value equals the variable of "FlyingStrength" and if the num varibale equals "1". Through an if statement, we then check if the row's value is "None". The reason being, some Pokemon have a Normal type which has a strength of "None", which means it has no strengths. If the Pokemon doesn't have Normal as a type, it then goes onto the else statement and appends all strengths to the strengths_1 list and increments the num variable to "2". Since the variable is now "2", the elif statement initiates and searches for the second Pokemon type and since we are using Zapdos, the second type will be "Electric". As for the first if statement, the same happens with searching for "None" and if not found, continues to add the strengths to the strengths_2 list.

![For Loop/If Statements To Add Each Type Strengths/Weaknessess to Their Own Lists](/docs/images/twotype3.png)

Once both lists have the strengths appended, another list is created titled "strength_list_all". Then for each list, a for loop iterates through the list and appends all the values to the "strength_list_all" list. Since different types can have the same strength and weaknesses, we then need to filter out the same strengths and weaknesses. To do this, we create a new variable titled "remove_duplicates" and assign the "strength_list_all" list encapsulated in the set class that only adds unique variables, instead of each and every varible in the list. 

![Add Unique Strength/Weaknessess To A List](/docs/images/twotype4.png)

Once we have the "remove_duplicates" list completed with unique varibles, we then use a for loop to append each variable from that list, to the "sentence" variable which was created early in the else statement, and is then printed as below:

"Strengths are: Water, Ground, Rock, Electric, Steel"

![Appending Each Varible From Remove_Duplicates List To Outputted Sentence](/docs/images/twotype5.png)

Now that the function has satisfied the requirements and finished, the same happens to the "view_weakness" function is essentially the same except differing variable and list names to match the weakness topic.

## Q7: Implementation Plan

Below shows that I had six main objectives. Five of those objectives relate to the programming of the project itself and the other is creating the Executable File as required.

![Trello board](/docs/images/trello1.png)

For the "Create an Exececutable File" task, below are the steps I created for me follow and complete:

![Create an Exececutable File Task](/docs/images/trello2.png)

For the "View_Strengths and View_Weakness Functions" task, below are the steps I created for me follow and complete:

![Create View_Strengths and View_Weakness Functions Task](/docs/images/trello3.png)

For the "Remove_Pokemon Function" task, below are the steps I created for me follow and complete:

![Create Remove_Pokemon Function Task](/docs/images/trello4.png)

For the "Add_Pokemon Function" task, below are the steps I created for me follow and complete:

![Create Add_Pokemon Function Task](/docs/images/trello5.png)

For the "View_Pokedex Function" task, below are the steps I created for me follow and complete:

![Create View_Pokedex Function Task](/docs/images/trello6.png)

For the "Create an Create a menu function that lists: View Pokedex, Add Pokemon, Remove Pokemon, Pokemon Strengths, Pokemon Weaknesses, Exit" task, below are the steps I created for me follow and complete:

![Create an Create a menu function that lists: View Pokedex, Add Pokemon, Remove Pokemon, Pokemon Strengths, Pokemon Weaknesses, Exit Task](/docs/images/trello7.png)

For all tasks, I added a bold "COMPLETE" to the end of each step to highlight which step was completed.

## R8: Help Documentation - How To Use The App

#### How to Install the Application

To install this application, please follow the below steps:
- Click [Here](https://github.com/Hader0/HaydenBradford_T1A3) to visit the Repository
- On the Repository page, there is a green code button, please see below for reference:
![Green Code Button](/docs/images/button.png)
- Click that button and select 'Download ZIP'.
- Once the file has been download, unzip that folder to a location of your choice.
- The Application is now installed!

**NOTE:** Before you run the application, move the types.csv file from the 'src' folder, outside and to the main/parent folder for the application to work.

- list.csv
- types.csv

#### Dependencies

**All that is needed is for Python 3 to be installed**.
All Libraries used are by included by default in Python.

#### How To Use The App

**NOTE:** Before you run the application, move the types.csv file from the 'src' folder, outside and to the main/parent folder for the application to work.

**To run the app, open the "run.sh" file located in the "src" folder.** Once the application is running, continue to read below.

This app, named "Pokedex", has 5 different choices. These choices are: View Pokedex, Add a Pokemon to your Pokedex, Remove a Pokemon from your Pokedex, See the strengths of a Pokemon and See the weaknesses of a Pokemon. Below is a picture of that menu:

![Pokedex Menu](/docs/images/menu.png)

To start off, you will have no Pokemon in your Pokedex. To add a Pokemon to your Pokedex, enter "2" on the line that states "Enter your selection:". Once you have entered that number, you will be presented with a option to enter your Pokemon name. This can be either a made-up name or an Official Pokemon. Once you have entered in a name, you will be presented with a question: "Does your Pokemon have one or two types? Enter 1 or 2:". For example, if you would like to add Zapdos to your Pokedex, you will need to enter "2". The Application then asks for you to enter in the Pokemon's first type. Since we are using Zapdos, we will enter in "Electric" for the first type. Then once the Application asks for the second type, we will enter in "Flying". Please see below to see an image of the code functioning

![Pokedex Add Pokemon Menu](/docs/images/addpokemonimg.png)

Now that a Pokemon is added, you can view what Pokemon you have in your Pokedex. To do this, enter "1" at the main menu where it asked to "Enter your selection". Once that is entered, it immediately shows each Pokemon and their types. Then you are shown how many Pokemon you have collected.

![Pokedex View Pokemon Menu](/docs/images/viewpokemonimg.png)

To see the strengths or weaknesses of a Pokemon, enter "4" to see the strengths or "5" to see the weaknesses. For the purpose of explanation, we will choose to enter "4" to see the strengths. Once you have entered in your selection, you will be prompted with: "Enter the Pokemon you would like to see the Strengths of:". We will enter Zapdos since we earlier added it to the Pokedex. The following is displayed.

![Pokedex View Strength/Weakness Menu](/docs/images/weaknessstrength.png)

To exit from the application, enter 6 into the "Enter your selection:" input and the application will end.