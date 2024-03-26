import requests

API_KEY = '60fdfcff605c48379d95f8dec1739b0f'
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
        print(recipes)
        print("\n")
        recipe_list = []

        params_inst = {
            'apiKey': API_KEY,
        }
        
        recipe_dict = {}

        for recipe in recipes:
            steps_list = []

            recipe_name = recipe['title']


            INST = f'https://api.spoonacular.com/recipes/{recipe["id"]}/analyzedInstructions'
            
            inst_response = requests.get(INST, params=params_inst).json()
            print("RESPONSE")
            print(inst_response)
            for step in inst_response[0]['steps']:
                steps_list.append(step['step'])

            recipe_dict[recipe_name] = steps_list
            print("inner----->")
            print(recipe_dict)
        print(recipe_dict)
        return recipe_dict

    else:
        print('Error fetching recipes:', response.status_code)

# get_recipes(ingredients)