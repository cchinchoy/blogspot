from flask import Flask, render_template
from flask import Blueprint
import requests

URL = "https://api.npoint.io/6446f4bf8b47a51f061c"


app = Flask(__name__)

data = requests.get(URL).json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", blog=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"]== index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)