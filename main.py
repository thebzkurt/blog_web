from flask import Flask, render_template, request
import requests

posts = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()

app = Flask("__name__")

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/home')
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)