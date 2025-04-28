from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/me")
def me():
    return render_template("me.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project")
def project():
    return render_template("project.html")

if __name__ == "__main__":
    app.run(debug=True)