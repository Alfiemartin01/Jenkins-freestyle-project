from apps import app
import apps.books as apbooks


@app.route('/')
def index():
    '''
    Main page of the flask app. 
    Gives a brief instructional text explaining how to use the program'''
    return('''Welcome to the Books database! 
        please add /<string> seperated by commas 
        to give the app information. \n
        the first item should be either one of the following: \n
           add - to add a new book with the rest of the information\n
           (followed by title,pages,isbn,gender,author)\n
           search - to search the next items in the list by author
        ''')

@app.route('/<inplist>')
def directing(inplist:str) -> str:
    '''
    checks to see if the input into the http link
    the first item in the comma seperated string parameter dictates if the search function is run for books or if a new book object is created.'''
    inplist = inplist.replace(", ",",")
    inplist = inplist.split(",")
    
    if inplist[0] == 'add':
        if len(inplist) == 5:
            apbooks.Book(inplist[1],inplist[2],inplist[3],inplist[4])
            return("Book added")
        elif len(inplist) == 6:
            apbooks.Book(inplist[1],inplist[2],inplist[3],inplist[4],inplist[5])
            return("Book added")
        else:
            return("Book unable to be added, parameters are not equal to the number of parameters")


    elif inplist[0] == 'search':
        asbooks = []
        for i in inplist[1:]:
            asbooks.append(f'{i}: {apbooks.Book.search(i)}\n')
        return("".join(asbooks))
    


        
