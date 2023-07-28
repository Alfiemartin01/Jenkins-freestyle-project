from apps import books

def test_books():

    #Initial variable tests
    assert books.books == [] 
    
    #__init__ tests

    #adding a single object tests
    b1 = books.Book('ILM',12,12,'Romance',"Athena")

    assert b1.title == 'ILM'
    assert b1.pages == 12
    assert b1.isbn == 12
    assert b1.genre == 'Romance'
    assert b1.author == 'Athena'
    assert books.books == [b1]

    #adding new object with different isbn and no author input given
    b2 = books.Book('ILW',14,14,'War') 
    assert books.books == [b1,b2]
    
    
    #adding new object with same isbn as b1
    b3 = books.Book('ILW',13,12,'Romcom',"Athens")
    
    assert b1.title == 'ILW'
    assert b1.pages == 13
    assert b1.isbn == 12
    assert b1.genre == 'Romcom'
    assert b1.author == 'Athens'
    assert books.books == [b1,b2]

    #__str__ tests 
    #testing githooks
    

    

