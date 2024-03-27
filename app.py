from flask import Flask, render_template, request, redirect, url_for
import recipe_finder, get_response

app = Flask(__name__)


inventory1=[]

sel_inventory =[]

ingredient_list = [['Apple', 3, 2], ['Orange', 5, 4]]

@app.route('/')
def index():
	return render_template('inventory.html', ingredients=ingredient_list)

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        items = request.form.get('ingredient')
        items = items.split(',')
        return render_template('recipe.html', recipe=recipe_finder.get_recipes(items))

    else:
         return render_template('recipe.html', recipe="")

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

    ing_list = []
    for ing in selected_ingredients:

         ing_list.append(''.join(letter for letter in ing if letter.isalpha()))

    return render_template('recipe.html', recipe=recipe_finder.get_recipes(ing_list))

if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=False)
