"""
У вас есть список.
[23, 16, 144, 72, 90, 11, 5]
Напишите три вьюшки
/first - выведет первое число
/last - выведет последнее число
/sum - выведет сумму чисел
"""
from flask import Flask
app = Flask(__name__)

my_list = [23, 16, 144, 72, 90, 11, 5]

@app.route('/first/')
def get_first():
    return str(my_list[0])

@app.route('/last/')
def get_last():
    return str(my_list[-1])

@app.route('/sum/')
def get_sum():
    return str(sum(my_list))

app.run(host='127.0.0.127', port=127)