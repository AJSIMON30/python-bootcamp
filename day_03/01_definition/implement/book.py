class Book:
    def __init__(self, title=None, genre=None, author=None):
        self.var1 = title
        self.var2 = genre
        self.var3 = author

    def __repr__(self):
        return f"{self.var1} {self.var2} {self.var3}"


book = Book("the hobbit", "fantasy" , "tolkie")
print(book)