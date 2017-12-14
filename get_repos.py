from __future__ import print_function
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from bokeh.plotting import figure, output_file, show
from flask.json import jsonify
import os
import json
import random

from flask import Flask
from flask import render_template

app = Flask(__name__)

redirect_uri = "http://127.0.0.1:5000/callback"
client_id = 'f11fe0bec06b5bf6a376'
client_secret = '376176a77e338c0c1f34f1db77c8d4fb871d5c9c'
oath_token = '5b5f193bd5207b639e99526319bc6de7a8e49b08'
url = 'https://api.github.com/user'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# This information is obtained upon registration of a new GitHub OAuth
# application here: https://github.com/settings/applications/new
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

language_list = []
name_list = []
repo_list = []
commit_list = []
stargazer_list = []
url_list = []
global url_data


@app.route("/")
def demo():
   # User Authorization.
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    session['oauth_state'] = state
    return redirect(authorization_url)


@app.route("/callback", methods=["GET"])
def callback():

    # Get and store access token
    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)
    session['oauth_token'] = token

    return redirect(url_for('.profile'))

@app.route("/graph", methods=["GET"])
def profile():
    data = {}
    github = OAuth2Session(client_id, token=session['oauth_token'])
    token = str(session['oauth_token'])
    overall_count = 0
    index = 1

    while overall_count <100:
        repos = github.get('https://api.github.com/search/repositories?q=stars%3A%3E1&sort=stars&order=desc&page='+str(index)+ '&per_page=100&rel="next"').json()
        for item in repos['items']:
            name_list.append(item['name'])
            repo_list.append(item['full_name'])
            stargazer_list.append(item['stargazers_count'])
            url_list.append(item['html_url'])
            overall_count += 1

        index +=1

    for item in repo_list:
        total_commits = 0
        commits = github.get('https://api.github.com/repos/'+item+"/stats/participation").json()
        #print(commits)
        if not commits:
            continue
        else:
            for item in commits['all']:
                total_commits += int(item)


        commit_list.append(total_commits)

    # prepare some data
    x = commit_list
    y = stargazer_list

    # output to static HTML file
    output_file('/Users/neasatang/PycharmProjects/P1/Python/CS3012/templates/index.html',title="Graph of the Top 100 GitHub Repositories in Star order")

    p = figure(plot_width=1000, plot_height=800)

    # create a new plot with a title and axis labels
    p = figure(title="Graph of the Top 100 GitHub Repositories in Star order", x_axis_label='Number of Commits', y_axis_label='Number of Stars')

    # add a circle renderer with a size, color, and alpha
    p.circle(x, y, size=20, fill_color=["firebrick","pink","blue","green", "navy","lilac","violet","cyan","yellow","darkolivegreen","paleblue",
                                   "lightslategray","lightskyblue","mistyrose","darkturquoise","deeppink","fuchsia","forestgreen","lavender",
                                   "khaki","lightsalmon","deepskyblue","paleturquoise","olive","coral","blueviolet"], alpha=0.6)

    names = name_list[:10]
    urls = url_list[:10]

    url_data = zip(names,urls)
    print(url_data)

    return render_template("index.html", url_data = url_data)


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['DEBUG'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True)

