from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route('/home')
def hello():
    return "<B>Hi This is a Flask Web app built using python and depoloyed on Azure Web App</B>"
