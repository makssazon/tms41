# Создать сайт. При запросе по урлу /my_word/[word],
# в случае если длина слова четна - выводит строку
# содержащую все нечетные элементы строки(abcde -> ace).
# В ином случае перенаправлять на домашнюю страницу.

from flask import Flask, redirect, url_for

from my_flask.flask_01 import time_now

app = Flask(__name__)

app.add_url_rule('/', 'home', time_now)


@app.route('/my_word/<string:word>')
def my_word(word):
    if len(word) % 2:
        return redirect(url_for('home'))
    else:
        return f'{word[::2]}'


if __name__ == '__main__':
    app.run()
