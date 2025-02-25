book= {}
def addbook(bookname,author,quantity):
    try:
        if not bookname in book:
            book[bookname] = {"author" : author, "quantity" : quantity} 
            print(f"Book named {bookname} added \n books are {book}")
        else:
            print(f"Book {bookname} already exist! Try again! ThankYou!")
    except Exception as e:
        print(f"Error Occured while execution error: {e}")

def removebook(book, bookname):
    if not bookname in book:
        print("Book does not exist! \n Please try again")
    else:
        book.pop(bookname)
        print(f"Book named {bookname} deleted \n Remaining books are {book}")
def availablebooks(book):
    for bookname,data in book.items():
        if data["quantity"] > 0 :
            pass
def searchbook(book, bookname):
    if not bookname in book:
        print("Book does not exist! \n Please try again")
    else:
        print(f"Book named {bookname} found details ")
        for bookn, detail in book.items():
            if bookn == bookname:
                print(f"Book author {detail["author"]}, quantity {detail["author"]} ")
def availablebooks(book,bookn):
    for bookname,data in book.items():
        if data["quantity"] > 0 :
            print(f"Book named {bookname} is available in {data["quantity"]} quantity")
def updatebook(book,bookname):
    counter = 0
    while counter < 3:
        if not bookname in book:
            print("Book does not exist! \n Please try again")
        else:
            inp = int(input("What Do you want to update \n Enter 1 to update author \n Enter 2 to update quantity "))
            inpvalue = input("Enter Your input value: ")
            values = book[bookname]
            if inp == 1:
                values["author"] = inpvalue
                print(f"Book Details are Name : {bookname}, Author {values["author"]}, Quantity {values["quantity"]} ")
                ch = int(input("Do you want to update anything else then input 1 or 2 for exit: "))
                if ch == 2:
                    break
            elif inp == 2:
                values["quantity"] = int(inpvalue)
                print(f"Book Details are Name : {bookname}, Author {values["author"]}, Quantity {values["quantity"]} ")
                break
            else:
                if counter < 3:
                    counter +=1
                    print(f"Please input correct option! Try again") 
                else:
                    print("You have exceded maxtries for reentries \nRun Program  Again! Thank you")
                    break
addbook("abc","ABC",10)
addbook("abd","ABD",20)
addbook("abc","ABC",10)
searchbook(book,"abc")
removebook(book,"abc")
availablebooks(book,"abd")
searchbook(book,"abc")
#updatebook(book,"abd")
#book = {'title':{"author":"quantity"}}


def borrowbook():
    pass
def returnbook():
    pass
def trackdue():
    pass