from flask import Flask, render_template, request, redirect, url_for
import json
import os    

app = Flask(__name__)

DB_FILE = "vote.json"

default_data = {
    "genres": {"Фэнтези": 0, "Детектив": 0, "Роман": 0, "Научная фантастика": 0, "Ужасы": 0},
    "authors": {"Достоевский": 0, "Агата Кристи": 0, "Джоан Роулинг": 0, "Стивен Кинг": 0, "Оруэлл": 0}
}

def load_data():
    """Функция для загрузки данных из файла"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return default_data
    return default_data

def save_data(data):
    """Функция для сохранения данных в файл"""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)


@app.route('/vote/<category>/<name>')
def vote(category, name):
    data = load_data()
    if category in data and name in data[category]:
        data[category][name] += 1
        save_data(data)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
