from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    returns hello world
    """
    return "<p>Hello, World!</p>"

@app.route('/dashboard')
def hello_dashboard():
    """
    navigates to dashboard
    """
    return "<h1>DASHBOARD</h2>"