

def store_book_array():
    Bookarray = []
    num_item = len(Bookarray)
    codeValidation = False

    while num_item <= 10:
        codeBook = ""
        while codeValidation == False:
            code = int(input("Please enter the numeric code of the book: "))
            if code in Bookarray:
                codeValidation = False
                print("* code is already in the database *")
            else:
                if code >= 100 and code <= 999:
                    codeBook = code
                    codeValidation = True
                else:
                    codeValidation = False
                    print("* The code must be in between 100 and 999 *")



        titlebook = input("Please enter the book title: ")
        authorbook = input("Please enter the author of the book: ")
        yearofbook = input("Please enter the year of publication of the book: ")

        Bookarray.append(codeBook)
        Bookarray.append(titlebook)
        Bookarray.append(authorbook)
        Bookarray.append(yearofbook)

        record_in_file(Bookarray)
        print_file()
        print(Bookarray)

        insert(hashTable, codeBook, titlebook, authorbook, yearofbook)

        print("///////")
        codeValidation = False
        Bookarray = []




def record_in_file(book):
    f = open("serial.txt", "a")

    f.write(str(str(book[0]) + " | " +str(book[1]) + " | " + str(book[2]) + " | " + str(book[3])))
    f.write("\n")
    f.close()


def print_file():
    f = open("serial.txt", "r")
    print("Book ID | Book Title | Main Author | Year Of Publication")
    for line in f:
        print(line)


hashTable = [[] for x in range(10)]

def insert(hashTable, bookID, bookTitle, mainAuthor, yearOfPub):
    hashKey = hash(bookID) % len(hashTable)
    keyExist = False
    Slot = hashTable[hashKey]

    Slot.append((bookID, bookTitle, mainAuthor, yearOfPub ))

def search(hashTable, key):
    hashKey = hash(key) % len(hashTable)
    Slots = hashTable[hashKey]

    for i, abcd in enumerate(Slots):
        a, b, c, d =abcd
        if key == a:
            return b

store_book_array()


