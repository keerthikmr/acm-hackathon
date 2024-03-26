# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
    app.debug = True
    app.run()
