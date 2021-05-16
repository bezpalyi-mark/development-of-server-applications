from json import JSONDecoder
from json import JSONEncoder


def from_json(json_object):
    return Book(json_object["title"], json_object["copyright_year"], json_object["authors"], json_object["cost"])


encoder = JSONEncoder()
decoder = JSONDecoder(object_hook=from_json)


class Book:
    def __init__(self, title, copyright_year, authors, cost):
        self.title = title  # str
        self.copyright_year = copyright_year  # int
        self.authors = authors  # list
        self.cost = cost  # float

    def __repr__(self) -> str:
        return f"\nTitle: {self.title}, Copyright year: {self.copyright_year}, " \
               f"Authors: {self.authors}, Cost: {self.cost}"

    def __str__(self) -> str:
        return f"Title: {self.title}, Copyright year: {self.copyright_year}, Authors: {self.authors}, Cost: {self.cost}"

    def write_to_file(self, filename):
        file = open(filename, "w")
        file.write(encoder.encode(self.__dict__))
        file.close()

    def read_from_file(self, filename):
        try:
            file = open(filename, "r")
            read_book = decoder.decode(file.read())
            file.close()

            self.title = read_book.title
            self.copyright_year = read_book.copyright_year
            self.authors = read_book.authors
            self.cost = read_book.cost
        except FileNotFoundError:
            print("File was not found")


class Library:
    books: []

    def get_books_in_cost_range(self, min_cost, max_cost):
        return list(filter(lambda book: min_cost <= book.cost <= max_cost, self.books))


def demo():
    library = Library()
    library.books = [
        Book("Structure and Interpretation of Computer Programs", 2021,
             ["Harold Abelson", "Gerald Jay Sussman", "Julie Sussman"], 40.41),
        Book("Design Patterns: Elements of Reusable Object-Oriented Software", 1994,
             ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"], 86.03),
        Book("Code: The Hidden Language of Computer Hardware and Software", 2020,
             ["Charles Petzold"], 24.70),
        Book("Cracking the Coding Interview: 189 Programming Questions and Solutions", 2014,
             ["Gayle Laakmann McDowell"], 22.94)
    ]
    print(f"All the books: {library.books}")
    print(f"\nBooks that costs between 23$ and 80$: {library.get_books_in_cost_range(23, 80)}")
    print(f"\nSaving first book to a file 'data.txt'...")
    library.books[0].write_to_file("data.txt")
    with open('data.txt', 'r') as file:
        print(f"File content: {file.read()}")
    print("\nRead saved book from 'data.txt' file and append it to books list")
    book_from_file = Book("", 0, [], 0.0)
    book_from_file.read_from_file("data.txt")
    library.books.append(book_from_file)
    print(f"\nAll the books: {library.books}")


demo()
