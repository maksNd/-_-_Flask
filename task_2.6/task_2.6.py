"""
У вас есть файл с записями журнала
Напишите вьюшку, которая при запросе
/profile/<user_id> вернет соответствующего пользователя.
"""
from flask import Flask

sourse = r'C:\Users\1\Desktop\доп_задачи_Flask\task_2.6\journal.txt'

app = Flask(__name__)


def get_data_from_txt_file(sourse: str):
    # data = []
    with open(sourse, encoding='utf-8') as file:
        data = [line for line in file]
        return data


data = get_data_from_txt_file(sourse)


@app.route('/profile/<int:pk>')
def get_profile_by_pk(pk):
    return str(data[pk - 1])


@app.route('/')
def page_hello():
    return "Hello"


app.run(host='127.0.0.2', port=1111)
