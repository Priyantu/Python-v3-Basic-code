book = []
book.append("C")
book.append("C++")
book.append("Java")
print(book)

book.pop()
print('Top book is ',book [- 1])

book.pop()
print('Top book is ',book [- 1])

book.pop()
if not book:
    print('No books left')