"""
Напишите три вьюшки которые обрабатывают обращения на адреса:
/hello - возврващает hello
/goodbye - возврващает goodbye
/seeyou - возвращает seeyou
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/hello/')
def page_hello():
    return "Hello"


@app.route('/goodbye/')
def page_goodbye():
    return "Goodbye"


@app.route('/seeyou/')
def page_seeyou():
    return "Seeyou"


app.run(host='127.0.0.5', port=7777)
