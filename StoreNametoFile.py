'''
Ask user about books in dictionary. And display a menu and store to file.
'''
#This Function will readFile to dicts.
def readFile (dicts, dataFile):
    for line in dataFile:
        line= line.strip()
        (title, price) = line.split(':')
        price = float(price)
        dicts[title]= price
#This function will add books to dicts.
def addBooks(dicts):
    title = input('Enter title: ')      
    while title !='':
        price = float(input('Enter price: '))
        dicts[title]=price
        title = input('Enter title: ')
        
#This function will print books in dictonary.
def printBooks(dicts):
    print('Current books')
    print(format('Book', '15s')+format('Price', '5s'))
    for title in dicts:
        print(format(title, '10s')+ format(dicts[title], '10.2f'))

#This function will find book and display price.        
def searchBooks(dicts):
    toFind = input('Enter book title: ')
    while toFind != '':
        if toFind in dicts:
            print('Cost of', toFind,format(dicts[toFind], '.2f'))
            print()
        else:
            print('We do not have', toFind)
            print()
        toFind = input('Enter book title: ')

#This function will take an order.    
def orders(dicts):
    n=0
    totalPrice = 0
    title = input('Enter title: ')    
    while title !='':
        if title in dicts:
            quan = int(input('Enter quantity: '))
            n = n+ quan
            totalPrice = totalPrice + quan*dicts[title]
        title = input('Enter title: ')

    print()
    print('Book order:')
    print('Total books:', n)
    print('Total cost: $'+ format(totalPrice, '.2f'))

#This function will search book in a price range.
def searchPrice(dicts):
    minN = float(input('Enter low limit: '))
    maxN = float(input('Enter high limit: '))
    print()
    print('Current books')
    print(format('Book', '15s')+format('Price', '5s'))
    for title in dicts:
        if dicts[title]>= minN and dicts[title] <= maxN:
            print(format(title, '10s')+ format(dicts[title], '10.2f'))
            
#This funcion will store dicts to file.
def saveBooks(dicts):
    outFile = open('books.txt', 'w')
    for title in dicts:
        outFile.write(title+':'+str(dicts[title])+ '\n')
    outFile.close

# This function will display a menu.    
def displayMenu():
    print()
    print('Menu')
    print('1 - Add Book')
    print('2 - Print all books')
    print('3 - Search for a book')
    print('4 - Taking an order')
    print('5 - Search by price')
    print('6 - Exit')
    print()
    choice = int(input('Enter Menu Choice:'))
    print()
    return choice



def main():
    books ={}
    dataFile = open('books.txt', 'r')
    readFile(books, dataFile)
    dataFile.close
    

    menuChoice = displayMenu()

    while menuChoice != 6:
        if menuChoice ==1:
            addBooks(books)
            
        elif menuChoice ==2:            
            printBooks(books)
            
        elif menuChoice ==3:            
            searchBooks(books)
            
        elif menuChoice ==4:            
            orders(books)
            
        elif menuChoice ==5:            
            searchPrice(books)
            
        menuChoice = displayMenu()

    saveBooks(books) 
    
main()
