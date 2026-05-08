from services.book_manager import BookManager
from services.category_manager import CategoryManager
from utils import show_menu # Lưu ý: nếu utils là file utils.py thì dùng 'from utils'

def main():
    book_manager = BookManager()
    cat_manager = CategoryManager()

    while True:
        show_menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            print("\n===== THÊM SÁCH =====")
            title = input("Tên sách: ")
            author = input("Tác giả: ")
            book_id = input("Mã sách: ")
            book_manager.add_book(title, author, book_id)

        elif choice == "2":
            book_manager.show_books()

        elif choice == "3":
            keyword = input("Nhập từ khóa tìm kiếm (Tên hoặc Mã sách): ")
            book_manager.search_book(keyword)

        elif choice == "4":
            print("\n===== THÊM THỂ LOẠI =====")
            cat_id = input("Mã thể loại: ")
            name = input("Tên thể loại: ")
            cat_manager.add_category(cat_id, name)

        elif choice == "5":
            cat_manager.show_categories()

        elif choice == "6":
            print("Đang thoát chương trình... Tạm biệt!")
            break
        else:
            print(">> Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6.")

if __name__ == "__main__":
    main()
