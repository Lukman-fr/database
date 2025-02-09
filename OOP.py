class Book:
    def __init__(self):
        self.books = []

    def add_book(self, name, copies):

        self.books.append({"name": name, "copies": copies})
        print(f"Book '{name}' with {copies} copies added.")

    def get_details(self):

        if not self.books:
            print("No books available.")
            return
        print("Available Books:")
        for book in self.books:
            print(f"Name: {book['name']}, Copies: {book['copies']}")

    def search_book(self, name):
        found_books = [book for book in self.books if book['name'].lower() == name.lower()]
        if found_books:
            for book in found_books:
                print(f"Found - Name: {book['name']}, Copies: {book['copies']}")
        else:
            print(f"Book '{name}' not found.")

if __name__ == "__main__":
    library = Book()

    library.add_book("Zola", 5)
    library.add_book("Kat Pencil", 10)
    library.add_book("Onontokal", 12)

    library.get_details()

    library.search_book("Zola")
    library.search_book("Deshe Bideshe")
    library.search_book("Onontokal")
