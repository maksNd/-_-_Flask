"""У вас есть текст
Напишите вьюшку /find/<слово>, которая вернет
"Да", если в тексте присутует <cлово>
"Нет", если не присутствует
"""

from flask import Flask

text = """
            На крыльце сидел котейка
            Мимо шел казах Андрейка
            Будет завтра у Андрейки
            из котейки тюбетейка
       """
app = Flask(__name__)

@app.route('/<word>')
def check_word(word) -> str:
    return "Да" if word in text else "Нет"


app.run(host='127.0.0.1', port=8888, debug=True)