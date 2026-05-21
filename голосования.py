import os
import json

# Имя файла базы данных
DB_FILE = "vote.json"

def clear_screen():
    if os.name == "nt":   
        os.system("cls")
    else:                 
        os.system("clear")

def save_data():
    """Сохраняет текущие результаты в JSON файл"""
    data = {
        "genres": genres_poll,
        "authors": authors_poll
    }
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    """Загружает данные из JSON файла, если он существует"""
    global genres_poll, authors_poll
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            genres_poll = data.get("genres", genres_poll)
            authors_poll = data.get("authors", authors_poll)

def vote_genre():
    print("\nВыберите любимый жанр:")
    genres = list(genres_poll.keys())  
    for i in range(len(genres)):
        print(i + 1, "-", genres[i])   

    try:
        choice = int(input("Введите номер жанра: "))
        if 1 <= choice <= len(genres):
            selected = genres[choice - 1]     
            genres_poll[selected] += 1        
            save_data()  # Сохраняем после изменения
            print("Спасибо большое вам за ваш голос!")
        else:
            print("Неверный выбор!")
    except ValueError:
        print("Пожалуйста, введите число.")

def vote_author():
    print("\nВыберите любимого писателя:")
    authors = list(authors_poll.keys()) 
    for i in range(len(authors)):
        print(i + 1, "-", authors[i])

    try:
        choice = int(input("Введите номер автора: "))
        if 1 <= choice <= len(authors):
            selected = authors[choice - 1]
            authors_poll[selected] += 1
            save_data()  # Сохраняем после изменения
            print("Спасибо большое вам за ваш голос!")
        else:
            print("Неверный выбор!")
    except ValueError:
        print("Пожалуйста, введите число.")

def show_results():
    print("\nРезультаты по жанрам:")
    for genre, votes in genres_poll.items():
        print(f"{genre}: {votes} голосов")

    print("\nРезультаты по авторам:")
    for author, votes in authors_poll.items():
        print(f"{author}: {votes} голосов")

def show_text_chart(data, title):
    print("\n", title)
    print("-" * 30)
    for option, votes in data.items():
        bar = "#" * votes
        print(f"{option:20} : {bar} ({votes})")

def main():
    # Загружаем данные перед началом цикла
    load_data()
    
    while True:
        clear_screen()  

        print("\n=== ОПРОС ПО КНИГАМ ===")
        print("1 - Проголосовать за жанр")
        print("2 - Проголосовать за автора")
        print("3 - Показать результаты")
        print("4 - Показать диаграмму жанров")
        print("5 - Показать диаграмму авторов")
        print("6 - Выход")

        choice = input("Выберите действие: ")

        clear_screen()  

        if choice == "1":
            vote_genre()
        elif choice == "2":
            vote_author()
        elif choice == "3":
            show_results()
        elif choice == "4":
            show_text_chart(genres_poll, "Популярность жанров")
        elif choice == "5":
            show_text_chart(authors_poll, "Популярность авторов")
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод!")
        
        input("\nНажмите Enter чтобы продолжить...")

if __name__ == "__main__":
    main()