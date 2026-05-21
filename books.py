import json
import os

DATA_FILE = "books.json"

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book():
    print("=== Добавление книги ===")
    # Заглушка
    pass

def show_all_books():
    print("=== Список книг ===")
    # Заглушка
    pass

def show_avg_rating():
    print("=== Средняя оценка ===")
    # Заглушка
    pass

def show_author_stats():
    print("=== Статистика по авторам ===")
    # Заглушка
    pass

def delete_book():
    print("=== Удаление книги ===")
    # Заглушка
    pass

def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        
        choice = input("Выберите пункт: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            show_avg_rating()
        elif choice == "4":
            show_author_stats()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()from datetime import datetime

def add_book():
    print("=== Добавление книги ===")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    
    # Проверка на дубликаты
    books = load_books()
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Ошибка: такая книга уже есть в трекере!")
            return
    
    while True:
        try:
            rating = int(input("Оценка (1-5): ").strip())
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5")
        except ValueError:
            print("Введите целое число")
    
    date_read = input("Дата прочтения (ГГГГ-ММ-ДД) или Enter для сегодняшней: ").strip()
    if not date_read:
        date_read = datetime.now().strftime("%Y-%m-%d")
    
    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date_read
    })
    
    save_books(books)
    print(f"Книга '{title}' добавлена!")
