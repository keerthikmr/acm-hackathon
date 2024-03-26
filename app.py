# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/suggest')
def suggest():
    return 'Suggest'


app.add_url_rule("/", "suggest", suggest)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
    app.debug = True
    app.run()
