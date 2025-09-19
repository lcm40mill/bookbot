from stats import (
    get_num_words,
    get_char_count,
    dict_sort
)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    sorted_chars = dict_sort(chars_dict)
    report(book_path, num_words, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")

main()