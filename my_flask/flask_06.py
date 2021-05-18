# Создать шаблон flask_06_form.html с формой Имя, фамилия, возраст.
# Создать вью /form: при GET запросе отображать форму, при POST
# запросе Выводить данные пользователю с помощью шаблона flask_06_display.html
import csv
import os

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'GET':
        return render_template('flask_06.html')
    else:
        user = list(request.form.values())
        with open('flask_06_users.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(user)
        return render_template('flask_06_display.html',
                               users=request.form, data=user)


if __name__ == '__main__':
    if not os.path.exists('flask_06_users.csv'):
        with open('flask_06_users.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = ['first name', 'last name', 'age']
            csvwriter.writerow(fields)
    app.run()
