from stats import get_number_of_words, get_letter_occurance, get_sorted_letter_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        lst = f.readlines()
        return ' '.join(lst)
    return ''

def main():
    args = sys.argv
    if len(args) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book = args[1]
    text = get_book_text(book)
    num_words = get_number_of_words(text)
    letter_count = get_letter_occurance(text)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book}...')
    print('----------- Word Count ----------')
    print('Found 75767 total words')
    print('--------- Character Count -------')
    # print(letter_count)
    sorted_list = get_sorted_letter_count(text)
    for entry in sorted_list:
        print(f'{entry["letter"]}: {entry["num"]}')
    print('============= END ===============')

main()