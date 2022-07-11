"""
Напишите три вьюшки которые обрабатывают обращения на адреса:
/one
/two
/three
Каждая вьюшка возврашает в соответствим со своим именем возврашает
из словаря слово на русском
words = {"one":"один", "two": "два", "three": "три"}
"""
from flask import Flask

app = Flask(__name__)

words = {"one": "один", "two": "два", "three": "три"}

@app.route('/num/<key>')
def get_from_dict(key: str) -> str:
    return words[key]

app.run(host='127.0.0.5', port=5000)
