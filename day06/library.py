import json
class Library:
  def __init__(self):
    self.books=[]

  def add(self,book):
    self.books.append(book)
    
  def remove(self,book):
    self.books.remove(book)
  
  def search(self,title):
    for book in self.books:
      if book.title==title:
        return book
    return None
  
  def find_by_author(self, author_name):
    result = []
    for book in self.books:
      if book.author.lower() == author_name.lower():
        result.append(book)
    return result
  
  def find_by_year(self, year):
    result = []
    for book in self.books:
      if book.year == year:
        result.append(book)
    return result

  def write_file(self):
    data=[book.to_dict() for book in self.books]
    with open("library.json","w") as f:
      json.dump(data,f)
  
  def read_file(self,library):
    with open("books.json","r") as f:
      data=json.load(f)
    self.books=[]
    for item in data:
      self.books.append(Book(item["title"],item["author"],item["year"]))
  
  
  def show(self):
    for book in self.books:
      print(book.title, book.author, book.year)
  
lib = Library()
lib.add(Book("1984", "George Orwell", 1949))
lib.add(Book("Animal Farm", "George Orwell", 1945))
lib.add(Book("Harry Potter", "J.K. Rowling", 1997))
print("ALL BOOKS:")
lib.show()

print("\nSEARCH:")
author=input("enter the author name")
for b in lib.find_by_author(author):
    print(b.title)
year=int(input("enter the year"))
for b in lib.find_by_year(year):
    print(b.title)
new_lib = Library()
new_lib.read_file("books.json")