import requests

API_KEY = '98a8a22da6004a6ea8287b51cf0e6c75'
ENDPOINT = 'https://api.spoonacular.com/recipes/findByIngredients'

ingredients = ['chicken', 'rice', 'broccoli']



def get_recipes(ingredients):

    params = {
        'apiKey': API_KEY,
        'ingredients': ','.join(ingredients),
        'number': 5,
    }

    response = requests.get(ENDPOINT, params=params)
    
    if response.status_code == 200:
        recipes = response.json()
        
        recipe_list = []

        for recipe in recipes:
            recipe_list.append(f"Recipe: {recipe['title']}")
        
        return recipe_list

    else:
        print('Error fetching recipes:', response.status_code)
