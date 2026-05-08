from services.book_manager import BookManager
from utils.menu import show_menu

manager = BookManager()

while True:
    show_menu()

    choice = input("Chọn chức năng: ")

    if choice == "1":
        print("\n===== THÊM SÁCH =====")

        title = input("Tên sách: ")
        author = input("Tác giả: ")
        book_id = input("Mã sách: ")

        manager.add_book(title, author, book_id)

    elif choice == "2":
        manager.show_books()

    elif choice == "3":
        keyword = input("Nhập từ khóa tìm kiếm: ")
        manager.search_book(keyword)

    elif choice == "4":
        print("Đang thoát chương trình...")
        break

    else:
        print(">> Lựa chọn không hợp lệ.")
