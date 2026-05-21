from flask import Flask, render_template, request, redirect, url_for
import json
import os    

app = Flask(__name__)

class VoteDatabase:
    def __init__(self, file_path):
        """Инициализация класса, задаем путь к файлу базы данных"""
        self.file_path = file_path
        self.default_data = {
            "genres": {"Фэнтези": 0, "Детектив": 0, "Роман": 0, "Научная фантастика": 0, "Ужасы": 0},
            "authors": {"Достоевский": 0, "Агата Кристи": 0, "Джоан Роулинг": 0, "Стивен Кинг": 0, "Оруэлл": 0}
        }

    def load_data(self):
        """Метод для загрузки данных из файла JSON"""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except:
                    return self.default_data
        return self.default_data

    def save_data(self, data):
        """Метод для сохранения обновленных данных в файл JSON"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_vote(self, category, name):
        """Метод для добавления голоса по выбранной категории и имени"""
        data = self.load_data()
        if category in data and name in data[category]:
            data[category][name] += 1
            self.save_data(data)
            return True
        return False

    def reset_data(self):
        """Метод для полной очистки (сброса) базы данных до начальных значений"""
        self.save_data(self.default_data)


db = VoteDatabase("vote.json")



@app.route('/')
def index():
    data = db.load_data()
    return render_template('index.html', data=data)


@app.route('/vote/<category>/<name>')
def vote(category, name):
    db.add_vote(category, name)
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    """Маршрут для сброса всех голосов"""
    db.reset_data()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)