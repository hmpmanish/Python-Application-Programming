# List of books: (title, author, year)
books = [
    ("Python Basics", "John Doe", 2019),
    ("Advanced Python", "Jane Smith", 2021),
    ("Data Science", "Alice Brown", 2020)
]

# Function to sort by year
def sort_books_by_year(book_list):
    return sorted(book_list, key=lambda x: x[2])

# Call function
sorted_books = sort_books_by_year(books)
print("Books sorted by publication year:")
for book in sorted_books:
    print(book)
