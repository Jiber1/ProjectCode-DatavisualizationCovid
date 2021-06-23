from flask import Flask, redirect, url_for, render_template, request
from os import path, environ
import pathlib
import scatterplot
import dataframes as data
import countygraph

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/search", methods=["POST","GET"])
def search():
    if request.method == "POST":
        day = request.form["day"]
        month = request.form["month"]
        stat = request.form["stat"]

        return redirect(url_for("plot", dy = day, mn = month, st = stat))
    else:
        return render_template("search.html")

@app.route("/<dy>/<mn>/<st>", methods=["POST","GET"])
def plot(dy, mn, st):
    if request.method == "POST":
        default = 'None'

        day = request.form.get('day', default)
        month = request.form.get('month', default)
        stat = request.form.get('stat', default)

        cnty = request.form.get('county', default)
        statc = request.form.get('statc', default)
        
        if(day != default and month != default and stat != default):
            return redirect(url_for("plot", dy = day, mn = month, st = stat))
        elif(cnty != default and statc != default):
            return redirect(url_for("county", county = cnty, st = statc))
    else:
        location = scatterplot.create_scatter(dy, mn, st)
        return render_template("scatter.html", scatter = location)

@app.route("/<county>", methods=["POST","GET"])
def county(county):
    location = countygraph.create_county('confirmed', county)
    return render_template("county.html", county = location)

@app.route("/countymap", methods=["POST", "GET"])
def countymap():
    return render_template("countymap.html")

if __name__ == "__main__":
    app.run()