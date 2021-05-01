import math
import string
from util.constants import Constants


def file_len(filepath):
    """
    Static function to return the number of lines in a given file
    :return:
    """
    num_lines = 0
    with open(filepath, encoding="utf-8") as f:
        for i in f:
            num_lines += 1
    return num_lines


def strip_whitespace_and_punctuation(word: str):
    """
    Static function to strip all whitespace and punctuation from a word. Also makes all letters lowercase.

    :param word: A string containing the word to strip whitespace and punctuation from.
    :return: A string containing the word, now all lowercase and with all whitespace and punctuation stripped out.
    """
    word = word.translate({ord(c): None for c in string.whitespace})
    word = word.translate(str.maketrans('', '', string.punctuation.join("“.”’")))
    word = word.lower()

    return word


class Reader:

    def __init__(self, book_path, num_threads, thread_index):
        """
        :param book_path: The filepath to the book that a given instance of Reader will read.
        :param starting_line: The line that the instance will start from, to make multithreading easier.
        :param num_threads: The number of threads we expect to use to process the book.
        """
        self.book_path = book_path
        self.num_threads = num_threads
        self.thread_index = thread_index
        self.average_length = 0
        self.longest_word = ""
        self.shortest_word = "pneumonoultramicroscopicsilicovolcanoconiosis"  # Longest word in the english language
        # according to oxford dictionary
        self.word_counts = {}
        self.total_word_lengths = 0
        self.number_of_words = 0
        self.most_common_word = ""

        with open(book_path, encoding="utf-8") as f:
            self.num_lines = int(f.readline())

    def add_word_to_counts(self, word: str):
        """
        Used to add a new word to the dictionary holding the word counts for the current reader.

        :param word: A string containing the word to add.
        :return: None
        """
        self.word_counts.update({word: 1})

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

        if len(word) > len(self.longest_word):
            self.longest_word = word

        if len(word) is not 0 and len(word) < len(self.shortest_word):
            self.shortest_word = word

        if not self.most_common_word == "":

            if self.word_counts.get(word) > self.word_counts.get(self.most_common_word):
                self.most_common_word = word

        else:
            self.most_common_word = word

    def process_line(self, line: str):
        """
        Processes a line of a book read in from a file. All appropriate statistics should be calculated and updated for
        the given line at the completion of this function's execution.

        :param line: A string containing the line to be processed.
        :return: None
        """

        line = line.replace("-", " ")
        line = line.replace("—", " ")
        split_line = line.split()

        for word in split_line:
            self.total_word_lengths += len(word)
            self.number_of_words += 1
            word = strip_whitespace_and_punctuation(word)
            if Constants.ignored_words.count(word) <= 0:
                self.process_word(word)

    def main(self):
        """
        Main function of the class. Called to perform the actual computation of the book statistics.
        :return: None
        """
        book_file = open(self.book_path, "r", encoding="utf-8")

        lines_to_process = (self.num_lines / self.num_threads)
        starting_line = 1 + math.floor(lines_to_process * self.thread_index)
        finishing_line = math.floor(starting_line + lines_to_process)

        for line_number, line in enumerate(book_file):
            if starting_line <= line_number <= finishing_line:
                self.process_line(line)

        self.average_length = self.total_word_lengths / self.number_of_words

        book_file.close()
