# Импортируем Flask для создания веб дизайна 
from flask import Flask, render_template, request, redirect, url_for
#Библиотека для работы с JSON
import json
#Библиотека для работы с файловой системой
import os    

#Создаем экземпляр приложения Flask
app = Flask(__name__)

#Пиременая с именем файла с базой данных
DB_FILE = "vote.json"

#Пустые данные, которые запишутся в файл, если он пуст или отсутствует(как запасной план или спательная палуба если файл vote.json что то случится)
default_data = {
    "genres": {"Фэнтези": 0, "Детектив": 0, "Роман": 0, "Научная фантастика": 0, "Ужасы": 0},
    "authors": {"Достоевский": 0, "Агата Кристи": 0, "Джоан Роулинг": 0, "Стивен Кинг": 0, "Оруэлл": 0}
}

def load_data():
    """Функция для загрузки данных из файла"""
    #Проверяем, существует ли файл на диске
    if os.path.exists(DB_FILE):
        #файл для чтения (r) в кодировке utf-8
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                #Пытаемся превратить текст из файла в словарь Python
                return json.load(f)
            except:
                #Если файл поврежден или пуст, возвращаем стандартные данные
                return default_data
    #Если файла вообще нет, возвращаем стандартные данные
    return default_data

def save_data(data):
    """Функция для сохранения данных в файл"""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#Главная страница сайта
@app.route('/')
def index():
    #Загружаем нынешние голоса из файла
    data = load_data()
    #Отправляем эти данные в HTML-шаблон index.html для обновления данных
    return render_template('index.html', data=data)

#Динамический маршрут для обработки голоса
#<category> — это либо genres, либо authors
#<name> — это название жанра или имя автора
@app.route('/vote/<category>/<name>')
def vote(category, name):
    #Загрузка свежих данных
    data = load_data()
    #Проверяем есть ли такая категория и такой вариант в нашей базе
    if category in data and name in data[category]:
        #Увеличиваем счетчик на 1
        data[category][name] += 1
        #Сохраняем обновленный результат обратно в файл
        save_data(data)
    #Возвращаем пользователя на главную страницу
    return redirect(url_for('index'))

#Запуск сервера
if __name__ == '__main__':
    #debug=True позволяет серверу самому перезагружаться при изменении кода
    app.run(debug=True)