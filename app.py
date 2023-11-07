from flask import Flask , render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def Connexion():
    return render_template('Connexion.html')

@app.route("/accueil")
def accueil():
    return render_template('accueil.html')

@app.route("/base/")
def base():
    return render_template("base.html")

if __name__=="__main__":
    app.run(debug=True)