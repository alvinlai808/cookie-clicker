from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/cookie_clicker', methods = ['POST'])
def cookie_time():
    return render_template('cookie_clicker.html')


app.run()