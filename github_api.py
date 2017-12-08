import sys
from github import Github

from flask import Flask
from flask import render_template
app = Flask(__name__)

redirect_uri = "http://127.0.0.1:5000/callback"

@app.route("/")
def index():
    g = Github(sys.argv[1], sys.argv[2])
    list=""

    for item in g.get_users(since=2017):
        print(item)

    print(list)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(host = '127.0.0.1') 