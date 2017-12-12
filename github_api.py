from __future__ import print_function
import sys
import requests
from github import Github
#import pymysql.cursors
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

redirect_uri = "http://127.0.0.1:5000/callback"
client_id = 'f11fe0bec06b5bf6a376'
client_secret = '376176a77e338c0c1f34f1db77c8d4fb871d5c9c'
oathToken = '3769b36306ab3a211cb266e593c5441000c953d3'
url = 'https://api.github.com/user'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# This information is obtained upon registration of a new GitHub OAuth
# application here: https://github.com/settings/applications/new
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

'''
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='githubdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

'''
@app.route("/")
def demo():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/callback", methods=["GET"])
def callback():
    # Step 3: Retrieving an access token.

    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token
    # in /profile.
    session['oauth_token'] = token

    return redirect(url_for('.profile'))


@app.route("/profile", methods=["GET"])
def profile():
    user_list = []
    location_list = []

    #github = OAuth2Session(client_id, token=session['oauth_token'])
    token = str(session['oauth_token'])
    header = {'Authorization: token ': token}
    username = requests.get('https://api.github.com/users').json()
   # username = github.get('https://api.github.com/users').json()
    for item in username:
        user_list.append(item['login'])
    print(len(user_list))

    github2 = OAuth2Session(client_id, token=session['oauth_token'])
    for location in location_list:
        place = github2.get('https://api.github.com/users/'+ location).json()
        location_list.append(place['location'])

    print(user_list)

   # users = github.get('https://api.github.com/users/:' + usernames)

    #for item in users:
    #    print(item)

    return 'hi'

'''
    try:
        with connection.cursor() as cursor:
            add_values = "INSERT INTO `users`(`name`, `place`) VALUES (%s, %s)"
'''



'''
    if users["location"] is None:
        continue
    else:

        cursor.execute(add_values, (user, github['location']))
        print("User: " + user + ", Place: " + github["location"])

connection.commit()

finally:
#connection.close()
return jsonify(github.get('https://api.github.com/users').json())
'''

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['DEBUG'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True)
