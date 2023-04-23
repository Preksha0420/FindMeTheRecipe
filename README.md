# FindMeTheRecipe
Two Data sources, Retrieval in Json format using API, Classes and caching components, Interactive Tree project

 The program suggests recipes based on user input and preferences. Run the FindMeTheRecipe.py file and follow the prompts to provide inputs to the program. To run the program successfully, please include the recipes.json, cuisine.txt, diet.txt and FindMeTheRecipe.py in the same directory on your computer. The project requires the use of the requests package and it must be installed prior to use. The API key used to retrieve data from the spoonacular API is included in the code and should not be changed. As a precautionary measure, only 150 requests can be made on the website everyday. To scale up the project, please contact prekshah@umich.edu.

To run the program, open a python console/command window and run the FindMeTheRecipe.py python script. Follow command line prompts to enter your preferred cuisine and dietary preference and finally enter a recipe name you like to search. 

The program will output a list of recipe suggestions, enter the “number” of the recipe you’d like to learn more. You can type in “exit” to quit the program. Then the program runs a tree to check if you have all the ingredients of the selected recipe. This is a yes/no tree. 

Finally, if you have all the ingredients for a certain recipe, the program will print the recipe instructions and give you an option to select any other “number” from the list of suggested recipes. You can type in “exit” to quit the program.
