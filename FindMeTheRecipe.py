import requests
import json

API_key = "0164c34b839d44d49c73e9ac07c4c0dc"

class Recipe:
    def __init__(self, i_d, title, image, calories, protein, fat, carbs, fiber):
        self.i_d = i_d
        self.title = title
        self.image = image
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        
# cuisine_tree = ("Would you like to explore our cuisines?", ("Would you like to have Indian food? ", ("Indian", None, None), ("Italian", None, None)), ("No worries, we will consider every cuisine! (Enter \"yes\" to continue)", None, None))

def tree_c(tree):
    """
    this function accepts a single argument, which is a tree, and
    plays the game once by using the tree to guide its questions. The function
    returns the user selected cuisine and a new tree that is the result of 
    playing the game on the  original tree and learning from the answers.

    Parameters
    ----------
    tree : A tuple of tuples ( a tree )
        A tuple of three tuples containing the following in order:
            1. A question.
            2. Response to the "YES" answer of the question.
            3. Response to the "NO" answer to the question.

    Returns
    -------
    cuisine: A string
        A string stating the cuisine the user would like to eat.
    tree : A tuple of tuples ( a tree )
        A tuple of three tuples containing the following in order:
            1. A question.
            2. Response to the "YES" answer of the question.
            3. Response to the "NO" answer to the question.

    """
    if tree[1] == None and tree[2] == None:
        # It is a leaf
        inp = input(tree[0] + ": ")
        if inp.lower() == "yes":
            # Save Indian food to a variable
            cuisine = tree[0]
            if cuisine == "No worries, we will consider every cuisine! (Enter \"yes\" to continue)":
                cuisine = None
            newTree = tree
        else:
            q1 = input("Drats! What cuisine would you like to eat? : ")
            # sen = "Would you like to have " + q1 + " food? " 
            sen = input("What differentiates between " + q1 + " and " + tree[0] + "? :")
            ans = input("And what's the answer for " + q1.lower() + "? : ")
            if ans.lower() == "yes":
                newTree = (sen, (q1, None, None), tree)
            elif ans.lower() == "no":
                newTree =  (sen, tree, (q1, None, None))
            cuisine = q1
        return cuisine, newTree
    else:
        inp = input(tree[0] + " : ")
        if inp.lower() == "yes":    
              c, t = tree_c(tree[1])
              tt = list(tree)
              tt[1] = t
              tree = tuple(tt)
        else:
              c, t = tree_c(tree[2])
              tt = list(tree)
              tt[2] = t
              tree = tuple(tt)
        return c, tree
        
# diet_tree = ("Would you like to explore our dietary options?", ("Would you like to have Vegetarian? ", ("Vegetarian", None, None), ("Chicken", None, None)), ("No worries, we will consider all diet options! (Enter \"yes\" to continue)", None, None))

def tree_d(tree):
    """
    this function accepts a single argument, which is a tree, and
    plays the game once by using the tree to guide its questions. The function
    returns the user selected diet and a new tree that is the result of 
    playing the game on the  original tree and learning from the answers.

    Parameters
    ----------
    tree : A tuple of tuples ( a tree )
        A tuple of three tuples containing the following in order:
            1. A question.
            2. Response to the "YES" answer of the question.
            3. Response to the "NO" answer to the question.

    Returns
    -------
    diet: A string
        A string stating the diet the user would like to eat.
    tree : A tuple of tuples ( a tree )
        A tuple of three tuples containing the following in order:
            1. A question.
            2. Response to the "YES" answer of the question.
            3. Response to the "NO" answer to the question.

    """
    if tree[1] == None and tree[2] == None:
        inp = input(tree[0] + ": ")
        if inp.lower() == "yes":
            diet = tree[0]
            if diet == "No worries, we will consider all diet options! (Enter \"yes\" to continue)":
                diet = None
            newTree = tree
        else:
            q1 = input("Drats! What's your dietary preference? (e.g. Chicken): ")
            sen = input("What differentiates between " + q1 + " and " + tree[0] + "? :")
            ans = input("And what's the answer for " + q1.lower() + "? : ")
            if ans.lower() == "yes":
                newTree = (sen, (q1, None, None), tree)
            elif ans.lower() == "no":
                newTree =  (sen, tree, (q1, None, None))
            diet = q1
        return diet, newTree
    else:
        inp = input(tree[0] + " : ")
        if inp.lower() == "yes":    
              c, t = tree_d(tree[1])
              tt = list(tree)
              tt[1] = t
              tree = tuple(tt)
        else:
              c, t = tree_d(tree[2])
              tt = list(tree)
              tt[2] = t
              tree = tuple(tt)
        return c, tree
           
def saveTree(tree, treeFile):
    """
    The function accepts a tree and a the handle of a file that is open for 
    writing, and saves the tree in that file. 
    
    Parameters
    ----------
    tree : A tuple of tuples ( a tree )
        A tuple of three tuples containing the following in order:
            1. A question.
            2. Response to the "YES" answer of the question.
            3. Response to the "NO" answer to the question.
    treeFile : file
        A file handle that is open for writing. The tree will be saved in this 
        file.

    Returns
    -------
    None.

    """
    if tree[1] == None and tree[2] == None:
        print("Leaf", file = treeFile)
        print(tree[0], file = treeFile)
        return 
    else:
        print("Internal Node", file = treeFile)
        print(tree[0], file = treeFile)
        saveTree(tree[1], treeFile)
        saveTree(tree[2], treeFile)

def loadTree(treeFile):
    """
    The function accepts a file that has already been opened for
    reading. It uses readline() to read one line at a time from the file, builds the tree
    described by that file, and returns it 

    Parameters
    ----------
    treeFile : file
        A file handle that is open for reading. The tree will be read and 
        loaded from this file.
        
    Returns
    -------
    tree : A tuple of tuples ( a tree )
        A tuple of three tuples containing the following in order:
            1. A question.
            2. Response to the "YES" answer of the question.
            3. Response to the "NO" answer to the question.

    """
    line = treeFile.readline()
    line = line.strip()
    if line.lower() == "internal node":
    # Create internal node
        node = treeFile.readline()
        node = node.strip()
        return (node, loadTree(treeFile), loadTree(treeFile))
    elif line.lower() == "leaf":
    # Create leaf
        leaf = treeFile.readline()
        leaf = leaf.strip()
        return (leaf, None, None)
     
CACHE_FILENAME = "recipes.json"
def open_cache():
    """
    opens the cache file if it exists and loads the JSON into
    a dictionary, which it then returns.
    if the cache file doesn't exist, creates a new cache dictionary
    Parameters
    ----------
    None
    Returns
    -------
    The opened cache
    
    """
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict):
    """
    saves the current state of the cache to disk
  Parameters
  ----------
  cache_dict: dict
  The dictionary to save
  Returns
  -------
  None
    """
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)
    fw.close()

def get_recipe_name(query, cuisine=None, diet=None, sort="calories", sortDirection="asc", number=10, limitLicense=True):
    """
    Calls the API and gets top suggeted recipes based on the input parameters

    Parameters
    ----------
    query : string
        This is the recipe search string that the user inputs to the program.
    cuisine : string, optional
        The user selected cuisine (from the tree). The default is None.
    diet : string, optional
        The user selected diet (from the tree). The default is None.
    sort : string, optional
        Sorts the recipe suggetions based on this. The default is "calories".
    sortDirection : string, optional
        "asc" or "dsc" to sort the recipies in ascending or descending. The default is "asc".
    number : int, optional
        Maximum number of suggested recipies. The default is 10.
    limitLicense : boolean, optional
        Whether the recipes should have an open license that allows display 
        with proper attribution.. The default is True.

    Returns
    -------
    recipes : dictionary
        A dictionary of suggested recipies.

    """
    baseurl = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + API_key
    parameters = {"query": query, "cusine": cuisine, "diet": diet, "sort": sort, "sortDirection": sortDirection, "number": number, "limitLicense": True}
    response = requests.get(baseurl, parameters)
    recipes = json.loads(response.text)
    if recipes["totalResults"] == 0:
        print("No recipes found, try again later!")
    return recipes

def print_recipe(recipes):
    """
    Print the suggested recipes in a user friendly format. Displays all nutritional information as well
    Parameters
    ----------
    recipes : list of objects of the Recipe class
        A list containing different suggested recipies stored as objects of the Recipe class.

    Returns
    -------
    None.

    """
    i = 1
    for recipe in recipes:
        print("-----------------------------------------------------------")
        print("Recipe: ", i)
        print("Title: " + recipe.title)
        print("Calories: "+ recipe.calories + " kcal")
        print("Protein: "+ recipe.protein + " g")
        print("Fats: "+ recipe.fat + " g")
        print("Carbs: "+ recipe.carbs + " g")
        print("Fiber: "+ recipe.fiber + " g")
        i += 1
        print("-----------------------------------------------------------")

def from_dict(d):
    """

    Parameters
    ----------
    d : dictionary
        A dictionary version of a recipe from the Recipe class.

    Returns
    -------
    Recipe object
        An object of the recipe class with attributes filled from the values 
        in the corresponding columns of the dicitonary d.

    """
    return Recipe(d["i_d"], d["title"], d["image"], d["calories"], d["protein"], d["fat"], d["carbs"], d["fiber"])

def print_steps(inst):
    """
    This function displays the recipe steps in a user friendly and numbered manner.

    Parameters
    ----------
    inst : dictionary
        A dictionary of the analyzed instructions of a particular recipe.

    Returns
    -------
    None.

    """
    i=0
    print("Recipe Steps: ")
    for num in inst[0]["steps"]:
        print(str(i+1) + ". " + num["step"])
        i+=1
    return

def get_ingredients(inst):
    """
    This function extracts the ingredients from the instructions dictionary and 
    outputs them as a list 

    Parameters
    ----------
    inst : dictionary
        A dictionary of the analyzed instructions of a particular recipe.

    Returns
    -------
    ing: list
        A list of unique ingredients used in the recipe    
    """
    
    ing = []
    for num in inst[0]["steps"]:
        for it in num["ingredients"]:
            if it["localizedName"] not in ing:
                ing.append(it["localizedName"])
    return ing
    
def play_tree(ing, i):
    """
    This function runs a tree with the ingredients for the user to check if 
    they have the necessary ingredients or not

    Parameters
    ----------
    ing : list
        A list of unique ingredients used in the recipe 
    
    i: int
        An iterative index to iterate in the ing list

    Returns
    -------
    boolean
        Return True if the user has all the ingredients
        Return False if the user is missing any of the ingredients.
    """
    q1 = input("Do you have " + ing[i] + "? : ")
    if q1.lower() == "yes":
        if ing[i] == ing[-1]:
            print("Great, follow these steps for the recipe!")
            return True
        return play_tree(ing, i+1)
    else:
        print("Sorry, but you cannot make this recipe!")
        return False
     
def get_cuisine():
    """
    A function that opens the cuisine.txt file, runs the tree and saves the 
    updated tree in the same cuisine.txt file

    Returns
    -------
    cuisine : string
        A string stating the cuisine the user would like to eat.

    """
    f_c = open("cuisine.txt", "r")
    cuisine_tree = loadTree(f_c)
    f_c.close()
    
    cuisine, c_tree = tree_c(cuisine_tree)
    
    tf_c = open("cuisine.txt", "w")
    saveTree(c_tree, tf_c)
    tf_c.close()
    return cuisine

def get_diet():
    """
    A function that opens the diet.txt file, runs the tree and saves the 
    updated tree in the same diet.txt file    

    Returns
    -------
    diet : string
        A string stating the diet the user would like to eat.

    """
    f_d = open("diet.txt", "r")
    diet_tree = loadTree(f_d)
    f_d.close()
    
    diet, d_tree = tree_d(diet_tree)
    
    tf_d = open("diet.txt", "w")
    saveTree(d_tree, tf_d)
    tf_d.close()
    return diet

if __name__ == "__main__":
    cuisine = get_cuisine()

    if cuisine == None:
        ci = " "
    else:
        ci = cuisine
    diet = str(get_diet())
    if diet == None:
        di = " "
    else:
        di = diet

    RECIPE_CACHE = open_cache()

    q = input("Enter a recipe you would like to search: ")
    if str(q.lower() + ci.lower() + di.lower()) in RECIPE_CACHE:
        recipes = [from_dict(d) for d in RECIPE_CACHE[str(q.lower() + ci.lower() + di.lower())]]
    else:
        rec = get_recipe_name(q, cuisine=cuisine, diet=diet)
        i_ds = [results["id"] for results in rec["results"]]
        titles = [results["title"] for results in rec["results"]]
        cals = [str(results["nutrition"]["nutrients"][0]["amount"]) for results in rec["results"]]
        pro = [str(results["nutrition"]["nutrients"][1]["amount"]) for results in rec["results"]]
        f = [str(results["nutrition"]["nutrients"][2]["amount"]) for results in rec["results"]]
        c = [str(results["nutrition"]["nutrients"][3]["amount"]) for results in rec["results"]]
        fib = [str(results["nutrition"]["nutrients"][4]["amount"]) for results in rec["results"]]
        img = [results["image"] for results in rec["results"]]
        
        recipes = [Recipe(i_ds[i], titles[i], img[i], cals[i], pro[i], f[i], c[i], fib[i]) for i in range(0, len(titles))]
        RECIPE_CACHE[str(q.lower() + ci.lower() + di.lower())] = [obj.__dict__ for obj in recipes]
        save_cache(RECIPE_CACHE)

    print_recipe(recipes)
    while True:   
        inp = input("Select one of these numbered recipes to make it or \"exit\" to exit the program: ")
    
        if inp.lower() == "exit":
            print("Thank you, bye!")
            break
        elif inp.isdigit():
            idd = str(recipes[int(inp)-1].i_d)
            RECIPE_CACHE = open_cache()
            if idd in RECIPE_CACHE:
                inst = RECIPE_CACHE[idd]
            else:
                search_url = "https://api.spoonacular.com/recipes/" + idd + "/analyzedInstructions/?apiKey=" + API_key
                response = requests.get(search_url)
                inst = json.loads(response.text)
                RECIPE_CACHE[idd] = inst
                save_cache(RECIPE_CACHE)
                
            # Cache inst using recipe_id and call from cache if id available.
            
            ing = get_ingredients(inst)
            print("Now let's see if you have all the ingredients!")
            flag = play_tree(ing, 0)
            if flag == True:
                print_steps(inst)
            else:
                print("Please check another recipe, thank you!")

