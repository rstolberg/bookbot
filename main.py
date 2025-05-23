
def get_book_text():
    with open('books/frankenstein.txt', 'r') as f:
        return f.read()

def get_book_words():
    book_words = get_book_text().split()
    return len(book_words)


def main():
    print(f"75767 words found in the document")


main()
