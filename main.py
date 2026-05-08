from services.book_manager import BookManager
from services.category_manager import CategoryManager
from utils.menu import show_menu 

def main():
    book_manager = BookManager()
    cat_manager = CategoryManager()

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
                book_manager.add_book(title, author, book_id)
                print(f">> Đã thêm sách '{title}' thành công!")

        elif choice == "2":
            book_manager.show_books()

        elif choice == "3":
            keyword = input("Nhập từ khóa tìm kiếm: ").strip()
            
            if keyword:
                book_manager.search_book(keyword) 
            else:
                print(">> Lỗi: Vui lòng nhập từ khóa để tìm kiếm!")

        elif choice == "4":
            print("Đang thoát chương trình...")
            break
            
        elif choice == "5":
            cat_manager.show_categories()

        else:
            print(">> Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()