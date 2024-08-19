"""
Magical Lookups - Library Software

Algorithm: page 401

Time complexity: O(m * n)
Auxiliary space: O(1)
"""

def connect_books_with_authors(books, authors):
    books_with_authors = []
    
    for book in books:
        # print(f'book = {book}')
        for author in authors:
            # print(f'author = {author}')
            if book.get('author_id') == author.get('author_id'):
                # print(f"book[author_id] = {book.get('author_id')}; author[author_id] = {author.get('author_id')}")
                books_with_authors.append({'book': book['title'], 'author': author['name']})
                
    return books_with_authors


if __name__ == '__main__':
    authors = [{'author_id': 1, 'name': 'Virginia Woolf'},
               {'author_id': 2, 'name': 'Leo Tolstoy'},
               {'author_id': 3, 'name': 'Dr Seuss'},
               {'author_id': 4, 'name': 'Rowline'},
               {'author_id': 5, 'name': 'Mark Twain'}]
    
    
    books = [{'author_id': 3, 'title': 'Hop on Pop'},
             {'author_id': 1, 'title': 'Mrs. Dalloway'},
             {'author_id': 4, 'title': 'Harry Potter'},
             {'author_id': 1, 'title': 'To the Lighthouse'},
             {'author_id': 2, 'title': 'Anna Karenina'},
             {'author_id': 5, 'title': 'The Adventures of Tom Sawyer'},
             {'author_id': 3, 'title': 'The Cat in the Hat'},
             {'author_id': 2, 'title': 'War and Peace'},
             {'author_id': 3, 'title': 'Green Eggs and Ham'},
             {'author_id': 5, 'title': 'The Adventures of Huckleberry Finn'}]
    
    
    print(connect_books_with_authors(books, authors))
    
    