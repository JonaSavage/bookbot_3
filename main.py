from stats import *

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    
    #print(text)
    print(f"There are {word_count} total words in this text.")
    print(char_count)


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        
    return text

main()