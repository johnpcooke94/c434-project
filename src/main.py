"""
This will be the main file to invoke when we want to run the program.
"""

import os
import threading
import time
from reader.reader import Reader
from reader.reader import file_len

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_book(book_path, num_threads, thread_index, thread_stats):
    reader = Reader(book_path, num_threads, thread_index)
    reader.main()
    thread_stats.update({threading.currentThread().name: [reader.total_word_lengths, reader.number_of_words,
                                                          reader.longest_word, reader.shortest_word,
                                                          reader.word_counts.get(reader.most_common_word)]})


def compute_statistics(thread_stats):
    total_word_lengths = 0
    number_of_words = 0
    longest_word = ""
    shortest_word = "pneumonoultramicroscopicsilicovolcanoconiosis"  # Longest word in the english language according
    # to oxford dictionary

    for thread in thread_stats:
        stats = thread_stats.get(thread)
        total_word_lengths += stats[0]
        number_of_words += stats[1]
        if len(stats[2]) > len(longest_word):
            longest_word = stats[2]
        if len(stats[3]) < len(shortest_word):
            shortest_word = stats[3]

    avg_word_length = round(total_word_lengths / number_of_words, 3)
    return [avg_word_length, longest_word, shortest_word, number_of_words]


def singlethreaded_read(book_file_name):
    book_path = os.path.join(CURRENT_DIR, "..", "books", book_file_name)
    thread_stats = {}

    # Create one thread
    new_thread = threading.Thread(target=read_book, args=(book_path, 1, 0, thread_stats))

    # Start single-threaded read of book
    new_thread.start()

    # Once the thread is finished, join it and compute stats
    new_thread.join()

    stats = compute_statistics(thread_stats)
    return stats


def singlethreaded():
    print("******************************** BEGIN SINGLETHREADED READ ******************************\n\n\n")

    # Compute Gatsby stats
    gatsby_start = time.time()
    stats = singlethreaded_read("gatsby.txt")
    gatsby_end = time.time()

    print("========================= The Great Gatsby Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Alice stats
    alice_start = time.time()
    stats = singlethreaded_read("alice_in_wonderland.txt")
    alice_end = time.time()

    print("========================= Alice in Wonderland Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Frankenstein stats
    frank_start = time.time()
    stats = singlethreaded_read("frankenstein.txt")
    frank_end = time.time()

    print("========================= Frankenstein Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Tale of Two Cities stats
    cities_start = time.time()
    stats = singlethreaded_read("tale_of_two_cities.txt")
    cities_end = time.time()

    print("========================= Tale of Two Cities Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Clarissa Harlowe stats
    clarissa_start = time.time()
    stats = singlethreaded_read("clarissa_harlowe.txt")
    clarissa_end = time.time()

    print("========================= Clarissa Harlowe Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    print("\n\n\n")

    times = [gatsby_end - gatsby_start, alice_end - alice_start, frank_end - frank_start, cities_end - cities_start,
             clarissa_end - clarissa_start]
    return times


def multithreaded_read(book_file_name):
    book_path = os.path.join(CURRENT_DIR, "..", "books", book_file_name)
    thread_stats = {}
    thread_list = []

    # Create as many threads as are available on the machine
    for i in range(os.cpu_count()):
        new_thread = threading.Thread(target=read_book, args=(book_path, os.cpu_count(), i, thread_stats),
                                      name=i)
        thread_list.append(new_thread)

    # Start threaded read of book
    for thread in thread_list:
        thread.start()

    # Wait for all threads to finish, then join them and compute statistics
    for thread in thread_list:
        thread.join()

    stats = compute_statistics(thread_stats)
    return stats


def multithreaded():
    print("******************************** BEGIN MULTITHREADED READ ******************************\n\n\n")

    # Compute Gatsby stats
    gatsby_start = time.time()
    stats = singlethreaded_read("gatsby.txt")
    gatsby_end = time.time()

    print("========================= The Great Gatsby Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Alice stats
    alice_start = time.time()
    stats = singlethreaded_read("alice_in_wonderland.txt")
    alice_end = time.time()

    print("========================= Alice in Wonderland Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Frankenstein stats
    frank_start = time.time()
    stats = singlethreaded_read("frankenstein.txt")
    frank_end = time.time()

    print("========================= Frankenstein Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Tale of Two Cities stats
    cities_start = time.time()
    stats = singlethreaded_read("tale_of_two_cities.txt")
    cities_end = time.time()

    print("========================= Tale of Two Cities Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    # Compute Clarissa Harlowe stats
    clarissa_start = time.time()
    stats = singlethreaded_read("clarissa_harlowe.txt")
    clarissa_end = time.time()

    print("========================= Clarissa Harlowe Statistics =========================")
    print("Average word length: " + str(stats[0]))
    print("Number of words: " + str(stats[3]))
    print("Longest word: " + str(stats[1]))
    print("Shortest word: " + str(stats[2]))

    print("\n\n\n")

    times = [gatsby_end - gatsby_start, alice_end - alice_start, frank_end - frank_start, cities_end - cities_start,
             clarissa_end - clarissa_start]
    return times


def main():
    multithread_start = time.time()
    mt_times = multithreaded()
    mulithreaded_end = time.time()

    singlethreaded_start = time.time()
    st_times = singlethreaded()
    singlethreaded_end = time.time()

    multithreaded_time = mulithreaded_end - multithread_start
    singlethreaded_time = singlethreaded_end - singlethreaded_start

    print("Total multithreaded time: " + str(multithreaded_time))
    print("Total singlethreaded time: " + str(singlethreaded_time))
    print()

    print("Gatsby times:")
    print("Multithreaded: " + str(mt_times[0]))
    print("Singlethreaded: " + str(st_times[0]))
    print()

    print("Alice times:")
    print("Multithreaded: " + str(mt_times[1]))
    print("Singlethreaded: " + str(st_times[1]))
    print()

    print("Frankenstein times:")
    print("Multithreaded: " + str(mt_times[2]))
    print("Singlethreaded: " + str(st_times[2]))
    print()

    print("Tale of Two Cities times:")
    print("Multithreaded: " + str(mt_times[3]))
    print("Singlethreaded: " + str(st_times[3]))
    print()

    print("Clarissa Harlowe times:")
    print("Multithreaded: " + str(mt_times[4]))
    print("Singlethreaded: " + str(st_times[4]))


if __name__ == "__main__":
    main()
