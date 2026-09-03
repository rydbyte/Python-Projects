from flask import Flask, request, render_template, url_for, redirect  
import jinja2, requests  

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/results")
def results():
    query = request.args.get("query") 
    nonalcoholic = request.args.get('nonalcoholic') 
    data = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}")  
    data = data.json()
    return render_template('results.html', data=data['drinks'], nonalcoholic=nonalcoholic)

@app.route("/info")
def info():
    query = request.args.get("query")
    data = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}")
    data = data.json()
    return render_template('info.html', data=data['drinks'][0])

if __name__ == "__main__":
    app.debug = True
    app.run()