"""
В одном килобайте содержится 1024 байта, в одном мегабайте 1024 килобайта.

Напишите вьюшку  /to_kbytes/<число>, которая переводит мегабайты в килобайты
Пример вывода: 6144

Напишите вьюшку  /to_bytes/<число>, которая переводит мегабайты в байты
Пример вывода: 6291456
"""
from flask import Flask

app = Flask(__name__)

@app.route('/to_kbytes/<int:megabytes>')
def convert_megabytes_to_kbytes(megabytes):
    return str(megabytes * 1024)

@app.route('/to_bytes/<int:megabytes>')
def convert_megabytes_to_bytes(megabytes):
    return str(megabytes * 1024 * 1024)

app.run(host='127.0.0.1', port=8888)