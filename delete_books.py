def delete_book():
    books = load_books()
    if not books:
        print("Нет книг для удаления.")
        return
    
    print("\n=== Список книг для удаления ===")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} - {book['title']}")
    
    try:
        index = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books(books)
            print(f"Книга '{removed['title']}' удалена!")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")
