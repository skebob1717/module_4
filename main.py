def show_all_books():
    books = load_books()
    if not books:
        print("Нет добавленных книг.")
        return
    
    print("\n=== Список книг ===")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} - {book['title']}")
        print(f"   Оценка: {book['rating']}/5, Дата: {book['date_read']}")

def show_avg_rating():
    books = load_books()
    if not books:
        print("Нет книг для подсчёта средней оценки.")
        return
    
    total = sum(book["rating"] for book in books)
    avg = total / len(books)
    print(f"Средняя оценка всех книг: {avg:.2f}")

def show_author_stats():
    books = load_books()
    if not books:
        print("Нет книг для статистики.")
        return
    
    stats = {}
    for book in books:
        author = book["author"]
        stats[author] = stats.get(author, 0) + 1
    
    print("\n=== Статистика по авторам ===")
    for author, count in stats.items():
        print(f"{author}: {count} книг(а/и)")
