import unittest
import os

import reader.reader as reader
from reader.reader import Reader

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestReaderMethods(unittest.TestCase):
    """
    Unit test class containing the methods that test the Reader class methods
    """

    def test_strip_whitespace(self):

        word = " “'\"\t\n\rHello."
        word = reader.strip_whitespace_and_punctuation(word)

        self.assertEqual("hello", word)