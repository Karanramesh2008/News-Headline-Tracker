from flask import Flask, render_template, request,redirect
import scraper
import storage

import scraper
app=Flask(__name__)
@app.route("/")
def home():
    headlines=scraper.get_headlines()
    return render_template("index.html",headlines=headlines)
@app.route("/save",methods=["POST"])
def save():
    headline=request.form["headline"]
    storage.save_headlines(headline)
    return redirect('/')

@app.route("/search")
def search():
    keyword=request.args.get("keyword","")
    headlines=scraper.get_headlines()
    results=scraper.search(headlines,keyword)
    return render_template("index.html",headlines=results)

@app.route("/saved")
def saved():
    keyword=storage.load_headlines()
    return render_template("saved.html",headlines=keyword)

def save():
    headline=request.form["headline"]
    storage.delete_headlines(headline)
    return redirect("/saved")

if __name__=='__main__':
    app.run(debug=True)