"""
Magical Lookups - Optimized Library Software

Bringing in the Extra Data Structure: The Hash Table

Algorithm: pages 402--403

Time complexity: O(m + n)
Auxiliary space: O(m)
"""


def connect_books_with_authors(books, authors):
    books_with_authors = []
    author_hash_table = {}  # the hash table uses up an additional O(m) space

    for author in authors:
        author_hash_table[author["author_id"]] = author["name"]

    for book in books:
        books_with_authors.append(
            {"title": book["title"], "author": author_hash_table[book["author_id"]]}
        )

    return books_with_authors


if __name__ == "__main__":
    authors = [
        {"author_id": 1, "name": "Virginia Woolf"},
        {"author_id": 2, "name": "Leo Tolstoy"},
        {"author_id": 3, "name": "Dr Seuss"},
        {"author_id": 4, "name": "Rowline"},
        {"author_id": 5, "name": "Mark Twain"},
    ]

    books = [
        {"author_id": 3, "title": "Hop on Pop"},
        {"author_id": 1, "title": "Mrs. Dalloway"},
        {"author_id": 4, "title": "Harry Potter"},
        {"author_id": 1, "title": "To the Lighthouse"},
        {"author_id": 2, "title": "Anna Karenina"},
        {"author_id": 5, "title": "The Adventures of Tom Sawyer"},
        {"author_id": 3, "title": "The Cat in the Hat"},
        {"author_id": 2, "title": "War and Peace"},
        {"author_id": 3, "title": "Green Eggs and Ham"},
        {"author_id": 5, "title": "The Adventures of Huckleberry Finn"},
    ]

    print(connect_books_with_authors(books, authors))
