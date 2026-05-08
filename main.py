from services.book_manager import BookManager
from utils.menu import show_menu

manager = BookManager()

while True:
    show_menu()

    choice = input("Chọn chức năng: ")

    if choice == "1":
        print("\n===== THÊM SÁCH =====")

        title = input("Tên sách: ").strip()
        author = input("Tác giả: ").strip()
        book_id = input("Mã sách: ").strip()

        if not title or not author or not book_id:
            print(">> Lỗi: Vui lòng nhập đầy đủ thông tin (Tên sách, Tác giả, Mã sách) không được để trống!")
        else:
            manager.add_book(title, author, book_id)
            print(f">> Đã thêm sách '{title}' thành công!")

    elif choice == "2":
        manager.show_books()

    elif choice == "3":
        keyword = input("Nhập từ khóa tìm kiếm: ").strip()
        
        if keyword:
            manager.search_book(keyword)
        else:
            print(">> Lỗi: Vui lòng nhập từ khóa để tìm kiếm!")

    elif choice == "4":
        print("Đang thoát chương trình...")
        break

    else:
        print(">> Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")