from flask import Flask, render_template
import reciper_finder

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html', recipe=reciper_finder.get_recipes(['chicken', 'rice', 'cabbage']))

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
