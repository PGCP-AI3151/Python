def printbook(book):
    for books in book:
            print(f'{books[0]} -> {books[1]}')

booklist =[['Java 8', 700], ['Python for Beginners', 500],['Data Structure',890]]

printbook(booklist)

print("-----Add New Book-----")
booklist.append(['MySql',350])
printbook(booklist)

print("-----Remove Entry Of Book-----")
booklist.pop(0)
printbook(booklist)

print("-----Update Price of Book-----")
booklist[0][1] = 1000
printbook(booklist)

print("-----Sort Books By Name-----")
booklist.sort()
printbook(booklist)

print("-----Sort Books By Price-----")
booklist.sort(key = lambda x:x[1])
printbook(booklist)

print("-----Maximum Price of Book-----")
max_priceBook = max(booklist , key = lambda x : x[1])
print(f'{max_priceBook[0]} -> {max_priceBook[1]}')

print("-----Minimum Price of Book-----")
min_priceBook = min(booklist,key = lambda x:x[1])
print(f'{min_priceBook[0]} -> {min_priceBook[1]}')