from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello(name = None):
    if name:
        return f'<h1>Hello, {name}!<h1>'
    else:
        return 'Hello, world!'