class Book:
    def __init__(self, title, author):
        if Book.is_valid_title(title):
            self.title = title
        else:
            self.title = "نامعتبر"
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.__mark_borrowed()

    def return_book(self):
        self.available = True

    def __mark_borrowed(self):
        self.available = False

    @staticmethod
    def is_valid_title(title):
        i = 0
        while i < len(title):
            c = title[i]
            if not (
                (c >= "a" and c <= "z")
                or (c >= "A" and c <= "Z")
                or (c >= "0" and c <= "9")
                or (c == " ")
            ):
                return False
            i += 1
        return True

    def __str__(self):
        if self.available:
            status = "موجود"
        else:
            status = "امانت داده شده"
        return (
            "کتاب: " + self.title + " | نویسنده: " + self.author + " | وضعیت: " + status
        )


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        count = 0
        i = 0
        while i < len(self.borrowed_books):
            count += 1
            i += 1

        if count < 3:
            if book.available:
                book.borrow()
                self.__add_to_list(book)

    def return_book(self, book):
        index = 0
        found = False
        while index < len(self.borrowed_books):
            if self.borrowed_books[index] == book:
                found = True
                break
            index += 1

        if found:
            book.return_book()
            del self.borrowed_books[index]

    def __add_to_list(self, book):
        self.borrowed_books.append(book)

    def __str__(self):
        result = "عضو: " + self.name + "\nکتاب‌های امانتی:\n"
        i = 0
        while i < len(self.borrowed_books):
            result += " - " + self.borrowed_books[i].title + "\n"
            i += 1
        return result


class PremiumMember(Member):
    def borrow_book(self, book):
        count = 0
        i = 0
        while i < len(self.borrowed_books):
            count += 1
            i += 1

        if count < 5:
            if book.available:
                book.borrow()
                self._Member__add_to_list(book)


book1 = Book("Python 101", "Ali Azimi")
book2 = Book("Intro to Algorithms", "Sara Jalali")
book3 = Book("C++ Guide", "Mohammad Reza")

student = Member("Navid")
vip = PremiumMember("Parisa")

student.borrow_book(book1)
student.borrow_book(book2)
print(student)

vip.borrow_book(book1)  # چون در دست student هست، نباید اضافه شود
print(vip)

student.return_book(book1)
vip.borrow_book(book1)
print(vip)
