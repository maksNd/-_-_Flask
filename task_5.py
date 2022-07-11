"""
У вас есть список слов в которых есть упоминания типа @cat
words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]
Напишите вьюшку /mentions, которая вытаскивает слова,
которые начинаются с собачки и возвращает их
Пример вывода:  кот хлеб подумай
"""
import random

from flask import Flask

app = Flask(__name__)

words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]

@app.route('/mentions/')
def get_word_with_symbol(symbol='@'):
    result = []
    for i in words:
        if i[0] == symbol:
            result.append(i)
            random.shuffle(result)
    print(" ".join(result))
    return " ".join(result)


app.run(host='127.0.0.10', port=8888)
