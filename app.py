# will use flask to render a template, redirecting to another url
# and create a url
from flask import Flask, render_template, redirect, url_for

# will use pymongo to interact with our mongo database
from flask_pymongo import PyMongo

# to use scraping code, will convert from Jupyter notebook to Python
import scraping

# flask setup
app = flask(__name__)

# use flask_pymongo to set up mongo connection
# tells Python that app wil connect to mongo using URI - uniform resource identifier
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define route for html page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# tell flask to run
if __name__ == "__main__":
    app.run()