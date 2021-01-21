n = int(input())
books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
want = max(books.values())
test = list()
for book,number in books.items():
    if number == want:
        test.append(book)
print(sorted(test)[0])
