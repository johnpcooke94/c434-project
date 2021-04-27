"""
This will be the main file to invoke when we want to run the program.
"""

import os
from reader.reader import Reader

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    book_path = os.path.join(CURRENT_DIR, "..", "books", "gatsby.txt")

    reader = Reader(book_path)
    reader.main()

    print(reader.word_counts)


if __name__ == "__main__":
    main()
