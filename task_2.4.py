"""
У вас есть список records = []

При каждом запросе на /add<word> добавляется <word> в список

При запросе на /show список выводится через запятую

Пример вывода: кот хлеб не ешь подумай
"""
import random

from flask import Flask

app = Flask(__name__)
records = []


@app.route('/add<word>')
def add_word(word):
    records.append(word)
    return f"Добавлено слово {word}"


@app.route('/show')
def show_words():
    random.shuffle(records)
    return ", ".join(records)


app.run(host='127.0.0.1', port=888)
