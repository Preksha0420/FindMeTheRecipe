# FindMeTheRecipe
Two Data sources, Retrieval in Json format, API, Classes & caching components, Interactive Tree project

 The program suggests recipes based on user input and preferences. Run the FindMeTheRecipe.py file and follow the prompts to provide inputs to the program. To run the program successfully, please include the recipes.json, cuisine.txt, diet.txt and FindMeTheRecipe.py in the same directory on your computer. The project requires the use of the requests package and it must be installed prior to use. The API key used to retrieve data from the spoonacular API is included in the code and should not be changed. As a precautionary measure, only 150 requests can be made on the website everyday. To scale up the project, please contact prekshah@umich.edu.

To run the program, open a python console/command window and run the FindMeTheRecipe.py python script. Follow command line prompts to enter your preferred cuisine and dietary preference and finally enter a recipe name you like to search. 

The program will output a list of recipe suggestions, enter the “number” of the recipe you’d like to learn more. You can type in “exit” to quit the program. Then the program runs a tree to check if you have all the ingredients of the selected recipe. This is a yes/no tree. 

Finally, if you have all the ingredients for a certain recipe, the program will print the recipe instructions and give you an option to select any other “number” from the list of suggested recipes. You can type in “exit” to quit the program.

## Data Structure:

The application stores and navigates through the necessary data using lists, dictionaries, classes, and trees. Diet.txt and Cuisine.txt are the two trees that the application starts with. In order to learn the user's preferences for food and nutrition, the program loads the current tree from these files and plays it for them. To ensure that any changes are taken into consideration, the application saves the trees to the.txt file. 

After that, we search the API for recipe recommendations using these parameters and the recipe search query. Each output recipe is saved as a "Recipes" class object. We keep the recipes for queries with multiple recipes as a list of objects. 

The final step is to look for particular recipe directions using the /analyzedInstruction command. The components and the steps in the recipe are two useful data items that this search returns. The steps are simply printed from the resulting dictionary once the ingredients are placed in a list (removing any duplicates stated in the API JSON). 

Finally, we cache the recipes.json file after saving all retrieved data in the proper dictionaries. The recipe ideas are first saved as the value of a "recipe name" + "cuisine" + "diet" key, and then the analyzed recipe instructions are saved as the value of a key called "recipe_id" that is unique to each recipe in the API.

Final Summary:

1. Use a tree to gather input from the user for their dietary preference, example Vegan, vegetarian etc.
2. Use a tree to gather input from the user for their preferred cuisine, example Italian, Mexican, Chinese, Indian etc.
3. A string input from the user regarding the recipe they would like to search for.
4. We retrieve data from the API for the top recommendations for this query/search string and save each of these recipes in a list of objects of the Recipe class previously defined.
5. Using this class and its attributes, we print the recipe name and ask user to select any one to learn more.
6. Once the user selects a number, we retrieve the recipe instructions and ingredients from the API and save the ingredients in a list.
7. We will cache the input query with the suggested recipes, the ingredients, and the recipe steps for future use.
8. Finally, after the user selects a number/recipe we will play a small tree with them to determine if they have all the ingredients required to make the meal or not. 
