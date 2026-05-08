from models.book import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(f">> Lỗi: Mã sách '{book_id}' đã tồn tại! Vui lòng dùng mã khác.")
                return 
        book = Book(title, author, book_id)
        self.books.append(book)
        print(f">> Thêm sách '{title}' thành công!")

    def show_books(self):
        if len(self.books) == 0:
            print(">> Danh sách sách trống.")
            return

        print("\n===== DANH SÁCH SÁCH =====")

        for index, book in enumerate(self.books, start=1):
            print(f"\n[Sách #{index}]")
            book.display()

    def search_book(self, keyword):
        found = False
        print(f"\n===== KẾT QUẢ TÌM KIẾM CHO '{keyword}' =====")

        for book in self.books:
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword == book.book_id
            ):
                book.display()
                found = True

        if not found:
            print(">> Không tìm thấy sách nào phù hợp.")