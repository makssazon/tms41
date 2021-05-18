# Создать сайт. При запросе по урлу /two_pow/[number]
# возвращает 2 в степени number
from my_flask.flask_01 import time_now
from flask import Flask

app = Flask(__name__)


@app.route('/two_pow/<int:number>')
def two_pow(number):
    assert isinstance(number, int)
    return f'2 ** {number} = {2 ** number}'


app.add_url_rule('/', 'time_now', time_now)

if __name__ == '__main__':
    app.run()
