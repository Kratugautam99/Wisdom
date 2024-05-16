class Library:
  def __init__(self):
    self.nobooks = 0
    self.books = []
  def addbook(self, book):
    self.books.append(book)
    self.nobooks = len(self.books)
  def aboutlib(self):
    print(f'''Total no. of books in the library is: {self.nobooks}.
The Books are as follows :''')
    i = 1
    for book in self.books:
      print(f"{i}) {book}")
      i += 1

K1 = Library()
K1.addbook("Emotional Intelligence")
K1.addbook("Rich Dad Poor Dad")
K1.addbook("How to win friends and influence people?")
K1.addbook("48 Laws of Power")
K1.aboutlib()
