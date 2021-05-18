# Создать сайт. При запросе на домашнюю страницу отображается текущая дата.
from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello world'


def time_now():
    return f'{datetime.now().date()}'


app.add_url_rule('/', 'time_now', time_now)

if __name__ == '__main__':
    app.run()
