'''
Create a class Book. Each book object should have the attributes: 
- title
- author (default unknown) 
- number of pages
- genre
- ISBN. 
The class should define the following methods:
- __init__ to set the attributes described above
- __str__ to print a description of the book
- a search method which returns all books by a given author (requires tracking of objects) - if there are no books by the given author return an empty list
- a method to check the validity of a given ISBN-13 - should return true if the ISBN is valid, false otherwise
As an additional stretch goal, create 2 subclasses for specific 
genres and override the __init__ method and __str__ methods appropriately
'''

books = []

class Book():
    ''' 
    This is the object to hold all the information about a book.

    variables include: title:str , pages:int , isbn:int , genre:str , [author:str]
    
    Methods include:
    __init__(self, title:str, pages:int, isbn:int, genre:str, author = "Unknown") ->None: Initialising the object with all the atrtributes
    __str__(self) -> None: outputs a string with title, pages, genre and author attributes
    valid_isbn(isbn:int) -> bool: used to check to see if the isbn already exists, if it exists it will return False
    search(author:str) -> list: used to search an author and return all the book object associated with the name

    '''
    def __init__(self, title:str, pages:int, isbn:int, genre:str, author = "Unknown") ->None:
        '''
        This method is used to initialise a new book object with all of the parameters as attributes.
        It will also add this object to the books list, so it can be recalled later.
        if the same book exists with the same isbn number. the old book object is edited instead with the new parameters.'''
        if all(isbn!=i.isbn for i in books):

            self.title = title
            self.pages = pages

            self.isbn = isbn
            self.genre = genre
            self.author = author
            books.append(self)
        else:
            for i in books:
                if i.isbn == isbn:
                    i.title = title
                    i.pages = pages
                    i.genre = genre
                    i.author = author

    @staticmethod
    def valid_isbn(isbn:int) -> bool:
        '''
        This method takes in an isbn and checks to see if a book object already has the same number.'''
        for i in books:
            if i.isbn == isbn:
                return True
        return False
        
    
    @staticmethod
    def search(author:str) -> list:
        '''
        This search method take in the name of an author and returns a list of all the titles of Book objects which match the author parameter.'''
        abooks = []
        for i in books:
            if i.author == author:
                abooks.append(i.title)
        return abooks

    def __str__(self) -> None:
        '''
        prints the title, author, genre and number of pages of a book.'''
        print(f"title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}")

