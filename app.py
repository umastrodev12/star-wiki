from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/story-of-starland")
def story_of_starland():
    return render_template ("story-of-starland.html")

@app.route("/creator")
def creator_about():
    return render_template ("creator.html")

if __name__=="__main__":
    app.run(debug=True)
