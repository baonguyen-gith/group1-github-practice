from book import BookManager
from utils import show_menu

manager = BookManager()

while True:
    show_menu()
    choice = input("Chọn chức năng: ")

    if choice == "1":
        title = input("Nhập tên sách: ")
        author = input("Nhập tác giả: ")
        book_id = input("Nhập mã sách: ")

        manager.add_book(title, author, book_id)

    elif choice == "2":
        manager.show_books()

    elif choice == "3":
        keyword = input("Nhập tên hoặc mã sách cần tìm: ")
        manager.search_book(keyword)

    elif choice == "4":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ!")
