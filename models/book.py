class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id

    def display(self):
        print(f"Mã sách   : {self.book_id}")
        print(f"Tên sách  : {self.title}")
        print(f"Tác giả   : {self.author}")
        print("-" * 30)


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, book_id):
        book = Book(title, author, book_id)
        self.books.append(book)
        print("Đã thêm sách thành công!")

    def show_books(self):
        if len(self.books) == 0:
            print("Danh sách sách trống!")
            return

        print("\n===== DANH SÁCH SÁCH =====")
        for book in self.books:
            book.display()

    def search_book(self, keyword):
        found = False

        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword == book.book_id:
                book.display()
                found = True

        if not found:
            print("Không tìm thấy sách.")
