from flask import Flask, request, render_template, redirect, url_for
from norm import *
import pickle

nlp_pipe = pickle.load(open('nlp_pipe.pkl', 'rb'))

app = Flask(__name__, template_folder = 'templates')
app.static_folder = 'static'

@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == "GET":
        return render_template("proekt.html")
    else:
        text = request.form['text']
        prediction = nlp_pipe.predict([text])[0]
        return redirect(url_for("index", pred=prediction))

app.run()