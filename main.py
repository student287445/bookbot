import sys

from stats import (
    get_num_words, 
    get_chars_dict, 
    get_sorted_list_of_dicts
)


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = args[1]
        file_contents = get_book_text(path)
        num_words = get_num_words(file_contents)
        chars_dict = get_chars_dict(file_contents)
        sorted_list = get_sorted_list_of_dicts(chars_dict)
        # print(f"{num_words} words found in the document")
        # print(chars_dict)
        # print(sorted_list[0])
        # print(sorted_list[1])
        # print(sorted_list[2])
        print_report(path, num_words, sorted_list)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

def print_report(book_path, word_count, sorted_char_count_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_count_list:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")


main()
