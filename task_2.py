"""
Напишите вьюшку /random, которая возвращает случайное число от 0 до 10
"""
import random
from flask import Flask

app = Flask(__name__)


@app.route('/random/')
def random_number():
    return str(random.randint(0, 10))


app.run(host='127.0.0.2', port=80)
