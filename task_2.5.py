"""
Напишите вьюшку, которая при запросе на /meal/борщ/стейк/компот вернет

На первое: борщ
На второе: стейк
На третье: компот
"""
from flask import Flask

app = Flask(__name__)

@app.route('/meal/<first>/<second>/<third>')
def get_meal(first, second, third):
    return f'<pre>' \
           f'На первое: {first}\n' \
           f'На второе: {second}\n' \
           f'На третье: {third}\n' \
           f'</pre>'

app.run(host='127.0.0.1', port=80)