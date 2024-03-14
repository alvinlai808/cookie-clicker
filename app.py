from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    num_clicks = 1
    return render_template('home.html', variable = num_clicks)    

app.run()