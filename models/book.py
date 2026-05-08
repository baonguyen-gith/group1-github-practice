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
        # 1. Kiểm tra mã sách đã tồn tại chưa
        for book in self.books:
            if book.book_id == book_id:
                print(f">> Lỗi: Mã sách '{book_id}' đã tồn tại! Không thể thêm mới.")
                return False # Trả về False để báo hiệu thêm thất bại
        
        # 2. Nếu chưa có thì tiến hành thêm sách
        new_book = Book(title, author, book_id)
        self.books.append(new_book)
        return True # Trả về True để báo hiệu thêm thành công

    def show_books(self):
        if len(self.books) == 0:
            print(">> Danh sách sách hiện đang trống!")
            return

        print("\n===== DANH SÁCH SÁCH =====")
        for book in self.books:
            book.display()

    def search_book(self, keyword):
        found = False
        print(f"\n===== KẾT QUẢ TÌM KIẾM CHO '{keyword}' =====")
        
        for book in self.books:
            # 3. Tìm kiếm theo Tên sách HOẶC Tác giả HOẶC Mã sách chính xác
            if (keyword.lower() in book.title.lower() or 
                keyword.lower() in book.author.lower() or 
                keyword == book.book_id):
                
                book.display()
                found = True

        if not found:
            print(">> Không tìm thấy sách nào phù hợp.")