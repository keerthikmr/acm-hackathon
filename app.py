from flask import Flask, render_template, request
import reciper_finder, get_response

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        items = request.form.get('ingredient')
        items = items.split(',')
        # return render_template('recipe.html', recipe=reciper_finder.get_recipes(items))

        return render_template('recipe.html', recipe={'Chicken Arrozcaldo': ['In a large soup pot over medium heat, saute garlic in olive oil until light brown.', 'Add ginger and onion, and saut for a minute.', 'Add chicken cube and stir until it melts.', 'Add chicken and stir-fry until both sides turn light brown.', 'Add fish sauce and simmer for another minute.', 'Add rice and water.', 'Mix well. Cover and simmer in medium heat for about 40 minutes or until the rice is fully cooked. Stir occasionally.', 'Put-in the hard boiled eggs', 'Add the safflower for additional color and aroma.', 'Stir in a small amount of sliced green onions.', 'Add salt and pepper if necessary.', 'If rice soup becomes too thick, add a little water to thin it a bit.', 'Garnish each bowl serving with sliced green onions and fried garlic just before serving.', 'Sprinkle a little lemon juice on the soup servings. (optional)'], 'Steamy Creamy Mushroom Risotto': ['Fry the chicken and the mushrooms and set aside.Fry the rice in a pan in the oil for a minute. Start boiling water and prepare the chicken broth in a separate saucepan.Start adding chicken broth water and the wine little by little to the rice and simmer at medium heat until the rice is cooked.Once the rice is done, add the butter, the chicken, and the mushrooms and blend them in.', 'Add the parmesan, salt, and pepper and stir one last time before you serve.'], 'Light and Chunky Chicken Soup': ['Place the chicken in a pot and add enough water to cover the chicken. Three quarters of the pot full.', 'Add the onion, carrot bits, salt pepper, rosemary, basil.Bring to the boil and allow to simmer until the chicken starts to pull away from the bone.', 'Remove the chicken from the pot and let it cool. Strip the meat off in tiny bite sized pieces.In the meantime, add the cup of rice to the stock and let it simmer for another 10 - 15 minutes. The rice must be well cooked.', 'Add the celery and the chicken to the soup.Allow to simmer for another 10 minutes.', 'Garnish with parsley.Ready to serve with some crispy hot bread or croutons on the side.'], 'SLOW COOKER CHICKEN GUMBO SOUP': ['Put all ingredients in crockpot and cook on high for 4 hours or low for 6 to 7 hours.'], 'Hydrabadi Dum Biriyani': ['Marinate the meat with curd, turmeric powder, biriyani masala, ginger garlic paste and salt overnight.', 'Heat ghee in a thick bottom pan add chicken and fry and cook meat until tender. Set meat aside', 'Add ghee, saute whole garam masala and cook rice until 90%% done; add salt and little saffrom milk for colour.', 'Remove from the flame when rice is cooked and no moisture is left.', 'In a thick-bottomed vessel, add the first layer of rice, half of the mint leaves, coriander and fried onions; pour ghee and saffron milk over it and cover the layer of rice with the meat.', 'Garnish with mint leaves, fried onions and coriander and saffron milk.', 'Cover the dish with foil and cover with heavy lid and cook on dum for 30-40 mins on medium heat.']})

    else:
         return render_template('recipe.html', recipe="")
    # return render_template('recipe.html', recipe=reciper_finder.get_recipes(['chicken', 'rice', 'cabbage']))

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=False)
