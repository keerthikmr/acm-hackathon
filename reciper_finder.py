# import requests

# API_KEY = '2eeab4c007dd414a84d729ef80c1f215'
# ENDPOINT = 'https://api.spoonacular.com/recipes/findByIngredients'

# ingredients = ['chicken', 'rice', 'broccoli']

# def get_recipes(ingredients):

#     params = {
#         'apiKey': API_KEY,
#         'ingredients': ','.join(ingredients),
#         'number': 5,
#     }

#     response = requests.get(ENDPOINT, params=params)
    
#     if response.status_code == 200:
#         recipes = response.json()

#         params_inst = {
#             'apiKey': API_KEY,
#         }

#         recipe_dict = {}

#         for recipe in recipes:
#             steps_list = []
#             used_ing = []
#             unused_ing = []

#             recipe_name = recipe['title']

#             INST = f'https://api.spoonacular.com/recipes/{recipe["id"]}/analyzedInstructions'
            
#             inst_response = requests.get(INST, params=params_inst).json()

#             for step in inst_response[0]['steps']:
#                 steps_list.append(step['step'])
            
#             unused = recipe['missedIngredients']
#             used = recipe['usedIngredients']

#             for ing in used:
#                 used_ing.append(ing['originalName'])
            
#             for ing in unused:
#                 unused_ing.append(ing['originalName'])

#             step_used_unused = {'steps': steps_list, 'used': used_ing, 'unused': unused_ing}

#             recipe_dict[recipe_name] = step_used_unused

#         print(recipe_dict)
#         return [recipe_dict, ingredients]

#     else:
#         print('Error fetching recipes:', response.status_code)

# # get_recipes(ingredients)