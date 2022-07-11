"""
У вас есть текст
content = "Кот это не хлеб, подумай, не ешь его, разработчик! Ай, ну я же просил"
Напишите вьюшки
/words - подсчитывает слова, например:  11 слов
/spaces - подсчитывает пробелы, например 10 пробелов
/letters – подсчитывает количество букв, например 35 букв
"""
from flask import Flask

app = Flask(__name__)
content = "Кот это не хлеб, подумай, не ешь его, разработчик! Ай, ну я же просил"


@app.route('/words/')
def get_words_count(content: str = content):
    return str((content.count(" ") + 1))


@app.route('/spaces/')
def get_spaces_count(content: str = content):
    return str((content.count(" ")))


@app.route('/letters/')
def get_letters_count(content: str = content):
    letters_counter = 0
    for i in content:
        if i.isalpha():
            letters_counter += 1
    return str(letters_counter)


app.run(host='127.0.0.255', port=8888)
