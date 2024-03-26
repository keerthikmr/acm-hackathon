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
        return render_template('recipe.html', recipe=reciper_finder.get_recipes(items))
    else:
         return render_template('recipe.html', recipe="")
    # return render_template('recipe.html', recipe=reciper_finder.get_recipes(['chicken', 'rice', 'cabbage']))

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=False)
