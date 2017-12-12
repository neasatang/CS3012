from __future__ import print_function
import sys
import requests
from github import Github
import pymysql.cursors

redirect_uri = "http://127.0.0.1:5000/callback"
client_id = 'f11fe0bec06b5bf6a376'
client_secret = '376176a77e338c0c1f34f1db77c8d4fb871d5c9c'
oathToken = 'f9f71476726ef177f8997b7f2edf65b835aa4f24'
url = 'https://api.github.com/users'
header = {'Authorization: token ' + oathToken}

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='githubdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

me = requests.get('https://api.github.com/user', auth=('neasatang', 'xXkulchickXx1'))
print(me)
requests.get('https://api.github.com/user?access_token=', oathToken)
users = requests.get('https://api.github.com/users','2017').json()
print(users)
g = Github(sys.argv[1], sys.argv[2])

try:
    with connection.cursor() as cursor:
        add_values17 = "INSERT INTO `user2017`(`name`, `place`) VALUES (%s, %s)"

        add_values16 = "INSERT INTO `user2016`('name', 'place') VALUES (%s, %s)"

        add_values15 = "INSERT INTO `user2015`('name', 'place') VALUES (%s, %s)"

        add_values14 = "INSERT INTO `user2014`('name', 'place') VALUES (%s, %s)"


        for item in g.get_users(2017):
            item = str(item)
            user = item.replace('NamedUser(login="', "")
            user = user.replace('")', "")
            r = requests.get('http://api.github.com/users/' + user).json()
            print(r)
            if r["location"] is None:
                continue
            else:
                cursor.execute(add_values17, (user, r['location']))
                print("User: " + user + ", Place: " + r["location"])

    connection.commit()

finally:
    connection.close()