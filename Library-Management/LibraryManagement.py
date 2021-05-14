import time

global bookInfo #variable type : list
global bookMaintain #variable type : dict

bookMaintain = {"AAA" : "Prathmesh", "FFF" : "Monu"}    #maintain who lends the book
bookInfo = ["Wings On Fire", "AAA", "BBB", "CCC", "FFF"]    #info of all books in library

class NiraliLibrary():
    """Main Header Class including all the methods to as mandatory
        1. lendBook('bookName', 'lenderName', lendTime = time (option))
        2. ReturnBacktoLibrary('bookname', 'lenderName', returntime = time)
        3. DonateBook('bookName', 'bookCondition', 'donatorName')
        4. AllInfo('bookName')
    ===========================================
        Info store as dict type in variable bookdict.
    """

    def __init__(self, bookDict, LibraryName):
        self.bookDict = bookDict    #to diplay all the books Name (Display Function).
        self.LibraryName = LibraryName  #to display the Library Name (Display Function).
    
    def lendBook(self):     #done
        bookName = input('Enter Book Name : ')
        lenderName = input("Enter Your Name : ")
        if bookName in bookInfo:
            bookMaintain[bookName] = lenderName
            print(f'You Successfully Lend {bookName}')
        else:
            print("No Such Book")
            if bookName in bookMaintain.keys():
                print(f"{bookName} is already lend by {bookMaintain.get(bookName)}")
            else:
                print(f"we don't have book with {bookName} Named")
    
    def ReturnBook(self):   #done
        bookName = input('Enter Book Name : ')
        lenderName = input('Enter UR Name : ')
        if bookName in bookMaintain.keys():
            if lenderName in bookMaintain.values():
                bookMaintain.pop(bookName)  #updated the bookMaintain 
                print(f"{bookName} Book Return. \nThanx for Returning Book")
            else:
                print('This book was lend by someone else, We the lender here...')
        else:
            print(f"{bookName} was not lend by any one")
        

    def DisplayBook(self):
        print(f" Welcome to {self.LibraryName} followinf are available books : ")
        print("---------------------------------------")
        for i in range(len(bookInfo)):
            print(f"\t|| {i} || {bookInfo[i]}")

    def DonateBook(self):
        bookName = input('Enter Book Name : ')
        donarName = input('Enter UR Name : ')
        if bookName not in bookInfo:
            bookInfo.append(bookName)
            print(f'Thank for the BOOK. {bookName} & Donar {donarName}')
        else:
            print("Thax but we already have this book")

l1 = NiraliLibrary(bookInfo, "NiraliLibrary")

while True:
    print("""Welcome to Nirali Book Shop
            1. Lend Book
            2. Return Book
            3. Display Books
            4. Donate Book
            5. Exit""")
    a = int(input('Enter Option : '))
    if a == 1:
        l1.lendBook()
    elif a ==2:
        l1.ReturnBook()
    elif a == 3:
        l1.DisplayBook()
    elif a == 4:
        l1.DonateBook()
    elif a ==5:
        exit()
    else:
        print("Worng Entry. Plz try again")