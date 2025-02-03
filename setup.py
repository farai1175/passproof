from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)




@app.route("/Grade8Math")
def Grade8Math():
    return render_template("Grade8Math.html")

@app.route("/Grade9Math")
def Grade9Math():
    return render_template("Grade9Math.html")

@app.route("/Grade10Math")
def Grade10Math():
    return render_template("Grade10Math.html")

@app.route("/Grade11Math")
def Grade11Math():
    return render_template("Grade11Math.html")

@app.route("/Grade12Math")
def Grade12Math():
    return render_template("Grade12Math.html")

@app.route("/Grade10PhSc")
def Grade10PhSc():
    return render_template("Grade10PhSc.html")

@app.route("/Grade11PhSc")
def Grade11PhSc():
    return render_template("Grade11PhSc.html")

@app.route("/Grade12PhSc")
def Grade12PhSc():
    return render_template("Grade12PhSc.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True)
