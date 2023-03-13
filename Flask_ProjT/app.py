from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('name')
    if username:
        return f'Hello, {username.upper()}!'
    else:
        return 'Please provide a name in the query parameter.'

if __name__ == '__main__':
    app.run()
