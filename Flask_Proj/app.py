#import flask
from flask import Flask, request
#Create the object with a parameter __name__
app = Flask(__name__)
#Create an END POINT using routes and bind them with a functionality
@app.route('/')
def home_page():
    return "Welcome to the HOME PAGE"

@app.route('/search')
def search_page():
    return "Welcome to the search page"

@app.route('/add')
def add_func():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))

#Run the app
if __name__ == '__main__':
    app.run(debug=True)
