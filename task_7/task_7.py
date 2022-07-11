"""
У вас есть файл JSON, где хранятся числа
Напишите три вьюшки
/first - выведет первое число
/last - выведет последнее число
/sum - выведет сумму чисел
"""
from flask import Flask

app = Flask(__name__)
import json

json_file = r'C:\Users\1\Desktop\доп_задачи_Flask\task_7\file_1.json'


def load_json_file(file: str = json_file):
    with open(json_file) as file:
        data = json.load(file)
        return data


data_from_json_file = load_json_file()


@app.route('/first/')
def get_first():
    return str(data_from_json_file[0])


@app.route('/last/')
def get_last():
    return str(data_from_json_file[-1])


@app.route('/sum/')
def get_sum():
    return str(sum(data_from_json_file))

app.run(host='127.1.1.1', port=1111)
