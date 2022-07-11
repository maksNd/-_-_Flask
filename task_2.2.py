"""
У вас если словарик, где ключи - это int
Напишите вьюшку  /city/<число>, которая будет возвращать
название города по его номеру в словаре
"""
from flask import Flask

app = Flask(__name__)

my_dict = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}

@app.route('/city/<int:key>')
def get_city_by_key(key):
    return my_dict[key]

app.run(host='127.0.0.1', port=80)