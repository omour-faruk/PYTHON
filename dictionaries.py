book = {

    'title' : 'Percy Jackson and the Sea of Monsters',
    'author' : 'Rick Riordan',
    'year' : 2013
}

print("Title:", book['title'])
print("Author:", book['author'])
print("Year:", book['year'])

book['genre'] = 'Greek Mythology'

print("\nBook information:")

for key, value in book.items():
    print(f"{key}: {value}")