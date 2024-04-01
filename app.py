from flask import Flask, render_template, request, redirect, url_for
import json
import os.path

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/cookie_clicker', methods = ['POST'])
def cookie_clicker():
    users = {}

    if os.path.exists('users.json'):
        with open('users.json') as users_file:
            users = json.load(users_file)

    if request.form['username'] not in users.keys():
        users[request.form['username']] = 0

    with open('users.json', 'w') as user_file:
        json.dump(users, user_file)

    return render_template(
        'cookie_clicker.html', 
        username=request.form['username'], 
        clicks=users[request.form['username']]
    )


@app.route('/update-click', methods = ['POST'])
def update_click():
    if os.path.exists('users.json'):
        with open('users.json') as users_file:
            users = json.load(users_file)

    users[request.form['username']] += 1

    with open('users.json', 'w') as user_file:
        json.dump(users, user_file)
    return render_template(
        'cookie_clicker.html', 
        username=request.form['username'], 
        clicks=users[request.form['username']]
    )


@app.route('/reset-cookies', methods = ['POST'])
def reset_cookies():
    if os.path.exists('users.json'):
        with open('users.json') as users_file:
            users = json.load(users_file)

    users[request.form['username']] = 0

    with open('users.json', 'w') as user_file:
        json.dump(users, user_file)
    return render_template(
        'cookie_clicker.html', 
        username=request.form['username'], 
        clicks=users[request.form['username']],
        reset=': Cookies have been reset'
    )


app.run(debug = True, host="localhost", port="8080")