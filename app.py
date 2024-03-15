from flask import Flask, render_template, request, redirect, url_for
import json
import os.path

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/cookie_clicker', methods = ['POST'])
def cookie_clicker():
    '''
    - New users will have default count of 0
    - After signing in, the count should resume from where the user left off
        - retrieve the user's last known count and display it
    - Every click sends a POST request to increment the particular user's count
    6:35pm
    '''
    users = {}

    if os.path.exists('users.json'):
        with open('users.json') as users_file:
            users = json.load(users_file)

    if request.form['username'] not in users.keys():
        users[request.form['username']] = 0

    with open('users.json', 'w') as user_file:
        json.dump(users, user_file)

    return render_template('cookie_clicker.html', username=request.form['username'])



app.run(debug = True, host="localhost", port="8080")