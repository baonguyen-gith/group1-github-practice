from models.book import Book


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, book_id):
        book = Book(title, author, book_id)
        self.books.append(book)
        print(">> Thêm sách thành công!")

    def show_books(self):
        if len(self.books) == 0:
            print("Danh sách sách trống.")
            return

        print("\n===== DANH SÁCH SÁCH =====")

        for index, book in enumerate(self.books, start=1):
            print(f"\nSách #{index}")
            book.display()

    def search_book(self, keyword):
        found = False

        for book in self.books:
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword == book.book_id
            ):
                book.display()
                found = True

        if not found:
            print(">> Không tìm thấy sách.")
