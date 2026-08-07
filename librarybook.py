books = {
    "Harry Potter": 3,
    "The Hobbit": 0,
    "1984": 2
}

print("Available books:")
for book in books:
    if books[book] > 0:
        print(book)

choice = input("Which book do you want to borrow? ")

if choice in books and books[choice] > 0:
    fee = float(input("Enter your late fee: "))
    books[choice] -= 1

    print("\nBook borrowed!")
    print("Late fee:", fee)

    print("\nLibrary stock:")
    for book in books:
        print(book, ":", books[book])
else:
    print("Sorry, that book is unavailable.")