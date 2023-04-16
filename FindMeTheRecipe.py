import requests
import json
# importing modules
import urllib.request
from PIL import Image
  
# urllib.request.urlretrieve(
#   'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
#    "gfg.png")
  
# img = Image.open("gfg.png")
# img.show()
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

def get_recipe_name(query, cuisine=None, excludeCuisine=None, diet=None, intolerance=None, equipment=None, includeIngredients=None, excludeIngredients=None, instructionsRequired=False, fillIngredients=False, addRecipeInformation=False, addRecipeNutrition=False, author=None, tags=None, recipeBoxId=0, maxReadyTime=100, ignorePantry=False, sort="calories", sortDirection="asc", minCarbs=0, minProtein=0, maxProtein=100, minCalories=0, minFat=0, maxFat=100, minAlcohol=0, minFiber=0, maxFiber=100, number=10, limitLicense=True):
    baseurl = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + API_key
    parameters = {"query": query, "cusine": cuisine, "diet": diet, "intolerance": intolerance, "equipment": equipment, "includeIngredients": includeIngredients, "excludeIngredients": excludeIngredients, "instructionsRequired": instructionsRequired, "fillIngredients": fillIngredients, "addRecipeInformation": addRecipeInformation, "addRecipeNutrition": addRecipeNutrition, "author": author, "tags": tags, "recipeBoxID": recipeBoxId, "maxReadyTime": maxReadyTime, "ignorePantry": ignorePantry, "sort": sort, "sortDirection": sortDirection, "minCarbs": minCarbs, "minProtein": minProtein, "maxProtein": maxProtein, "minCalories": minCalories, "minFat": minFat, "maxFat": maxFat, "minFiber": minFiber, "maxFiber": maxFiber, "number": number, "limitLicense": True}
    response = requests.get(baseurl, parameters)
    recipes = json.loads(response.text)
    if recipes["totalResults"] == 0:
        print("No recipes found, try again later!")
    return recipes

def print_recipe(recipes):
    i = 1
    for recipe in recipes:
        print("-----------------------------------------------------------")
        print("Recipe: ", i)
        print("Title: " + recipe.title)
        # print(recipe.image)
        print("Calories: "+ recipe.calories + " kcal")
        print("Protein: "+ recipe.protein + " g")
        print("Fats: "+ recipe.fat + " g")
        print("Carbs: "+ recipe.carbs + " g")
        print("Fiber: "+ recipe.fiber + " g")
        i += 1
        print("-----------------------------------------------------------")

def from_dict(d):
    return Recipe(d["i_d"], d["title"], d["image"], d["calories"], d["protein"], d["fat"], d["carbs"], d["fiber"])

def print_steps(inst):
    i=0
    print("Recipe Steps: ")
    for num in inst[0]["steps"]:
        print(str(i+1) + ". " + num["step"])
        i+=1
    return

def get_ingredients(inst):
    ing = []
    for num in inst[0]["steps"]:
        for it in num["ingredients"]:
            if it["localizedName"] not in ing:
                ing.append(it["localizedName"])
    return ing
    
def play_tree(ing, i):
    q1 = input("Do you have " + ing[i] + "? : ")
    if q1.lower() == "yes":
        if ing[i] == ing[-1]:
            print("Great, follow these steps for the recipe!")
            return True
        return play_tree(ing, i+1)
    else:
        print("Sorry, but you cannot make this recipe!")
        return False
          
if __name__ == "__main__":
    RECIPE_CACHE = open_cache()
    
    q = input("Enter a recipe you would like to search: ")
    if q.lower() in RECIPE_CACHE:
        recipes = [from_dict(d) for d in RECIPE_CACHE[q.lower()]]
    else:
        rec = get_recipe_name(q)
        
        i_ds = [results["id"] for results in rec["results"]]
        titles = [results["title"] for results in rec["results"]]
        cals = [str(results["nutrition"]["nutrients"][0]["amount"]) for results in rec["results"]]
        pro = [str(results["nutrition"]["nutrients"][1]["amount"]) for results in rec["results"]]
        f = [str(results["nutrition"]["nutrients"][2]["amount"]) for results in rec["results"]]
        c = [str(results["nutrition"]["nutrients"][3]["amount"]) for results in rec["results"]]
        fib = [str(results["nutrition"]["nutrients"][4]["amount"]) for results in rec["results"]]
        img = [results["image"] for results in rec["results"]]
        
        recipes = [Recipe(i_ds[i], titles[i], img[i], cals[i], pro[i], f[i], c[i], fib[i]) for i in range(0, len(titles))]
        RECIPE_CACHE[q] = [obj.__dict__ for obj in recipes]
        dumped_json_cache = json.dumps(RECIPE_CACHE)
        save_cache(RECIPE_CACHE)

    print_recipe(recipes)
    while True:   
        inp = input("Select one of these numbered recipes to make it or \"exit\" to exit the program: ")
    
        if inp.lower() == "exit":
            print("Thank you, bye!")
            break
        elif inp.isdigit():
            idd = str(recipes[int(inp)-1].i_d)
            search_url = "https://api.spoonacular.com/recipes/" + idd + "/analyzedInstructions/?apiKey=" + API_key
            response = requests.get(search_url)
            inst = json.loads(response.text)
            ing = get_ingredients(inst)
            print("Now let's see if you have all the ingredients!")
            flag = play_tree(ing, 0)
            if flag == True:
                print_steps(inst)
            else:
                print("Please check another recipe, thank you!")
