from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects.html")
def projects():
    return render_template("projects.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/blog.html")
def updates():
    return render_template("updates.html")

@app.route("/timeline.html")
def timeline():
    return render_template("timeline.html")



if __name__ == "__main__":
    app.run(debug=True)