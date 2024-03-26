from flask import Flask, render_template, request, redirect, url_for
import recipe_finder, get_response

app = Flask(__name__)


inventory1=[]

sel_inventory =[]

ingredient_list = [['Apple', 2, 2], ['Orange', 5, 4]]

@app.route('/')
def index():
	return render_template('inventory.html', ingredients=ingredient_list)

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        items = request.form.get('ingredient')
        items = items.split(',')
        return render_template('recipe.html', recipe=recipe_finder.get_recipes(items))

#         return render_template('recipe.html', recipe=
# [{'Chicken Arrozcaldo': {'steps': ['In a large soup pot over medium heat, saute garlic in olive oil until light brown.', 'Add ginger and onion, and saut for a minute.', 'Add chicken cube and stir until it melts.', 'Add chicken and stir-fry until both sides turn light brown.', 'Add fish sauce and simmer for another minute.', 'Add rice and water.', 'Mix well. Cover and simmer in medium heat for about 40 minutes or until the rice is fully cooked. Stir occasionally.', 'Put-in the hard boiled eggs', 'Add the safflower for additional color and aroma.', 'Stir in a small amount of sliced green onions.', 'Add salt and pepper if necessary.', 'If rice soup becomes too thick, add a little water to thin it a bit.', 'Garnish each bowl serving with sliced green onions and fried garlic just before serving.', 'Sprinkle a little lemon juice on the soup servings. (optional)'], 'used': ['rice', 'add chicken and stir until it melts', 'add rice and water. mix well. cover and simmer in heat'], 'unused': ['garlic', 'onion', 'thumb sized ginger', 'chicken cube', 'fish sauce', 'green onion', 'hardboiled quail eggs', 'pcs lemon', 'in a soup pot over heat', 'stir in a amount of green onions. add salt and pepper if necessary', 'sprinkle a little lemon juice on the soup']}, 'Steamy Creamy Mushroom Risotto': {'steps': ['Fry the chicken and the mushrooms and set aside.Fry the rice in a pan in the oil for a minute. Start boiling water and prepare the chicken broth in a separate saucepan.Start adding chicken broth water and the wine little by little to the rice and simmer at medium heat until the rice is cooked.Once the rice is done, add the butter, the chicken, and the mushrooms and blend them in.', 'Add the parmesan, salt, and pepper and stir one last time before you serve.'], 'used': ['chicken', 'rice'], 'unused': ['butter', 'chicken broth', 'mushrooms', 'onion', 'parmesan', 'bell pepper', 'white wine']}, 'Light and Chunky Chicken Soup': {'steps': ['Place the chicken in a pot and add enough water to cover the chicken. Three quarters of the pot full.', 'Add the onion, carrot bits, salt pepper, rosemary, basil.Bring to the boil and allow to simmer until the chicken starts to pull away from the bone.', 'Remove the chicken from the pot and let it cool. Strip the meat off in tiny bite sized pieces.In the meantime, add the cup of rice to the stock and let it simmer for another 10 - 15 minutes. The rice must be well cooked.', 'Add the celery and the chicken to the soup.Allow to simmer for another 10 minutes.', 'Garnish with parsley.Ready to serve with some crispy hot bread or croutons on the side.'], 'used': ['basmati rice', 'chicken'], 'unused': ['carrot', 'celery finelly', 'basil', 'rosemary', 'parsley', 'a onion', 'bell pepper']}, 'SLOW COOKER CHICKEN GUMBO SOUP': {'steps': ['Put all ingredients in crockpot and cook on high for 4 hours or low for 6 to 7 hours.'], 'used': ['chicken', 'rice'], 'unused': ['can chicken broth', 'carrot', 'bell pepper', 'onion', 'canned tomatoes', 'okra', 'cajun seasoning', 'hot sauce']}, 'Hydrabadi Dum Biriyani': {'steps': ['Marinate the meat with curd, turmeric powder, biriyani masala, ginger garlic paste and salt overnight.', 'Heat ghee in a thick bottom pan add chicken and fry and cook meat until tender. Set meat aside', 'Add ghee, saute whole garam masala and cook rice until 90%% done; add salt and little saffrom milk for colour.', 'Remove from the flame when rice is cooked and no moisture is left.', 'In a thick-bottomed vessel, add the first layer of rice, half of the mint leaves, coriander and fried onions; pour ghee and saffron milk over it and cover the layer of rice with the meat.', 'Garnish with mint leaves, fried onions and coriander and saffron milk.', 'Cover the dish with foil and cover with heavy lid and cook on dum for 30-40 mins on medium heat.'], 'used': ['basmati rice', 'chicken biriyani masala'], 'unused': ['leg pieces', 'onions', 'garam masala', 'turmeric powder', 'ginger garlic paste', 'coriander & mint leaves', 'ghee as required', 'saffron strands dissolved warm milk', 'egg & fried onions']}}, ['Apple', 'Orange']])

    else:
         return render_template('recipe.html', recipe="")
    # return render_template('recipe.html', recipe=reciper_finder.get_recipes(['chicken', 'rice', 'cabbage']))

@app.route('/some', methods=['GET', 'POST'])
def some():
     if request.method == 'POST':
        items = request.form.get('hidden-recipe')
        if (items != None):
            test_str = ''.join(letter for letter in items if letter.isalnum() or letter == ',')

            converted_list = test_str.split(',')

            return render_template('useItems.html', ingredients=converted_list)
        else:
             items = request.form.get('hidden-ing')
             if (items != None):
                test_str = ''.join(letter for letter in items if letter.isalnum() or letter == ',')

                converted_list = test_str.split(',')
                
                global ingredient_list
                reduced_list = []
                for item in converted_list:
                    reduced = request.form.get(f"{item}-quantity")
                    reduced_list.append([item, reduced])
                
                for ingre in ingredient_list:
                    for red_ingre in reduced_list:
                        if ingre[0] == red_ingre[0]:
                            ingre[1] = int(ingre[1]) - int(red_ingre[1])

             return render_template('inventory.html', ingredients=ingredient_list)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html', ingredients=ingredient_list)

@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    global ingredient_list
    new_ingredient = request.form.get('newIngredient')
    quantity = int(request.form.get('quantity'))
    expiration = int(request.form.get('expiration'))

    ingre = [new_ingredient, int(quantity), int(expiration)]
    
    ingredient_list.append(ingre)

    return render_template('inventory.html', ingredients=ingredient_list)

@app.route('/add_to_inventory', methods=['POST'])
def add_to_inventory():
    selected_ingredients = request.form.getlist('ingredient')
    print("ingreeee", selected_ingredients)

    ing_list = []
    for ing in selected_ingredients:

         ing_list.append(''.join(letter for letter in ing if letter.isalpha()))

    print("Selected ingredients:", ing_list)

    # ingredient_list = []
    # for i in ing_list:
    #     ingredient_list.append(i[0])
    # ingredient_list = ing_list    
    # print(ingredient_list)

    return render_template('recipe.html', recipe=recipe_finder.get_recipes(ing_list))
    # return render_template('recipe.html', recipe="")

if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=False)
