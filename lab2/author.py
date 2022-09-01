
# main - runs various tests to see if the Author class, and its publish method are working correctly.
def main():
    sam = Author('Sam DaMan')
    sam.publish('book')
    print(sam)
    sam.publish('book')
    jam = Author('Jam Jamajamjam')
    jam.publish('jam\'s jam on jammin jam from jammin jams')
    print(jam)
    jam.publish('Jam forgot to name this book so this is the book title')
    print(jam)
    jam.publish('JAM')
    print(jam)
    jam.publish('JAM')

# This is the author class - it takes a name, but does not require a book as author's may not have published anything at that moment.  It also has checks for if the
# list has anything in it - which will print the list, or if the list is blank - it will print a message saying no books.  This also has the publish method, which is
# used to add books that the author has published to the book list.  If a book already exists, and that same title is attempted again, it will not add and print a message
# saying it was already added.
class Author:
    
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def __str__(self):
        #variation
        # titles = ', '.join(self.books) or 'No published books'    
        # return f'{self.name}. Books: {titles}'

        if self.books:
            book_list = ', '.join(self.books)
        else: 
            book_list = 'No books'
        return f'Author name: {self.name}, Published books: {book_list}'

    def publish(self, book):
        if book in self.books:
            print('Sorry, this book has already been added.')
        else:
            self.books.append(book)




main()