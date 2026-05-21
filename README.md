ENG
BookVote - Web application for book poll
A modern web application based on Flask for conducting an interactive poll among readers. The project allows users to vote for their favorite literary genres and authors through a stylish web interface, automatically saving and updating the results in real time.

Technologies used:
Python- the main programming language (server logic).
Flask- a lightweight web framework for creating a back-end and handling HTTP requests.
Jinja2- a built-in template engine in Flask for dynamically rendering data in HTML.
HTML/CSS (Grid & Flexbox)- responsive interface layout with Dark Mode (dark theme) support.
JSON- a built-in text database for persistent storage of results.

Project Structure

text
Project Folder/
 │
 ├── 📁 .vscode/              # Editor settings and launch configurations
 ├── 📁 templates/
 │    └── 📄 index.html        # Main web interface (HTML structure & CSS styles)
 │
 ├── 📄 app.py                # Main backend server script (Flask Application)
 ├── 📄 vote.json             # Database file storing the vote counts in JSON format
 ├── 📄 requirements.txt      # Text file listing all third-party dependencies
 ├── 📄 голосования.py        # Alternative terminal-based polling script (CLI)
 └── 📄 README.md             # Project documentation (this file)

Installation & Launch Guide
1. Install Dependencies
To run the web interface, you need to install the required libraries listed in the dependencies file. Open your terminal in VS Code and run:
<py -m pip install -r requirements.txt>

2. Verify Installation
To ensure that the framework and its requirements were successfully installed, you can verify the Flask version using:
<python -m flask --version>

3. Run the Web Application
Execute the main server file app.py to launch the backend and initialize the web interface:

<py app.py>

4. Open the Website
Once launched successfully, the following status line will appear in your terminal:
* Running on http://127.0.0.1:5000

Hold down the Ctrl key and click the left mouse button (Ctrl + LMB) on the link, or manually copy and paste the address http://127.0.0.1:5000 into your preferred web browser.

Note: The project also retains an alternative голосования.py script. This is a fully functional, self-contained terminal version of the poll. It reads and writes to the exact same database file (vote.json), meaning any votes cast in the terminal environment will instantly reflect on the website interface!


 
RU
BookVote - Веб-приложение для книжного опроса
Современное веб-приложение на базе Flask для проведения интерактивного опроса среди читателей. Проект позволяет пользователям отдавать голоса за любимые литературные жанры и авторов через стильный веб-интерфейс, автоматически сохраняя и обновляя результаты в режиме реального времени.

Используемые технологии:
Python- основной язык программирования (логика сервера).
Flask- легкий веб-фреймворк для создания серверной части и обработки HTTP-запросов.
Jinja2- встроенный во Flask шаблонизатор для динамического вывода данных в HTML.
HTML/CSS (Grid & Flexbox)- адаптивная верстка интерфейса с поддержкой Dark Mode (темной темы).
JSON- встроенная текстовая база данных для постоянного хранения результатов.

Структура проекта
text
 коды по пайтону/
 │
 ├── 📁 .vscode/              # Editor settings and launch configurations
 ├── 📁 templates/
 │    └── 📄 index.html        #Веб-интерфейс приложения (HTML + CSS стили)
 │
 ├── 📄 app.py                #Основной серверный код (Flask-приложение)
 ├── 📄 vote.json             #База данных проекта в формате JSON
 ├── 📄 requirements.txt      #Текстовый файл со списком всех сторонних библеотек
 ├── 📄 голосования.py        #Резервная консольная версия опроса (CLI)
 └── 📄 README.md             #Документация проекта

1. Установка фласк
Для работы веб-интерфейса необходимо установить микрофреймворк Flask. Откройте терминал в VS Code и выполните команду:
<py -m pip install flask>

2. Проверка установки
Чтобы убедиться, что фреймворк успешно установлен, проверьте его версию командой:
<python -m flask --version>

3. Запуск веб-приложения
Запустите файл app.py, который отвечает за работу веб-сервера и визуальной части проекта:
<py app.py>

4. Переход на сайт
После успешного запуска в терминале появится строка:
< * Running on http://127.0.0.1:5000 >
Зажмите клавишу Ctrl и кликните левой кнопкой мыши (Ctrl + ЛКМ) по ссылке, либо скопируйте адрес http://127.0.0.1:5000 в любой браузер.
P.s
Примечание: В проекте также сохранен файл голосования.py. Это полностью рабочая автономная консольная версия опроса. Она использует общую базу данных vote.json, поэтому голоса, оставленные в терминале, мгновенно отобразятся и на сайте!