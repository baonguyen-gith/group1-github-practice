class Category:
    def __init__(self, cat_id, name):
        self.cat_id = cat_id
        self.name = name

    def display(self):
        print(f"Mã TL: {self.cat_id} | Tên thể loại: {self.name}")
