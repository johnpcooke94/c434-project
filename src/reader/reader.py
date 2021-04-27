from util.constants import Constants


class Reader:

    def __init__(self, book_path):
        self.book_path = book_path
        self.average_length = 0
        self.longest_word = ""
        self.shortest_word = ""
        self.word_counts = {}

    def add_word_to_counts(self, word: str):
        """
        Used to add a new word to the dictionary holding the word counts for the current read.

        :param word: A string containing the word to add.
        :return: None
        """
        self.word_counts.update({word: "1"})

    def iterate_word_count(self, word: str):
        """
        Used to iterate the word count of a word that is already present in self.word_count.

        :param word: A string containing the word the count of which is to be iterated. The word **must** already be
        present in the list.
        :return: None
        """

        count = int(self.word_counts.get(word))
        count += 1
        self.word_counts.update({word: count})

    def process_word(self, word: str):
        """
        Processes a word read in from a line.

        :param word: A string containing the word to be processes.
        :return: None
        """
        if self.word_counts.get(word) is None:
            self.add_word_to_counts(word)

        else:
            self.iterate_word_count(word)

    def process_line(self, line: str):
        """
        Processes a line of a book read in from a file. All appropriate statistics should be calculated and updated for
        the given line at the completion of this function's execution.

        :param line: A string containing the line to be processed.
        :return: None
        """

        split_line = line.split()

        for word in split_line:
            if Constants.ignored_words.count(word) <= 0:
                self.process_word(word)

    def main(self):
        book_file = open(self.book_path, "r", encoding="utf-8")


        for line in book_file:
            self.process_line(line)

