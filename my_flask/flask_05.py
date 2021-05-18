# Создать папку templates в корне проекта.
# Создать шаблон flask_05.html с формой Имя,
# фамилия, возраст. Создать вью /form:
# при GET запросе отображать форму, при POST
# запросе дописывать переданные данные в файл.

import csv
import os

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'GET':
        return render_template('flask_05.html')
    else:
        user = list(request.form.values())
        with open('flask_05_users.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(user)
        return f"""user {user[0]} {user[1]} {user[2]} added to file
    <form action="http://localhost:5000/add_user" method="get">
    <p>if you want to add new user </p>
    <input type="submit" value="press this button">"""


if __name__ == '__main__':
    if not os.path.exists('flask_05_users.csv'):
        with open('flask_05_users.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = ['first name', 'last name', 'age']
            csvwriter.writerow(fields)
    app.run()
