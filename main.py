from stats import *

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    char_count_sorted = sorted_char_count(char_count)
    
    #print(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"There are {word_count} total words in this text.")
    print("--------- Character Count -------")
    for i in char_count_sorted:
        print(f"{i["char"]}: {i["count"]}")
    #print(char_count)


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        
    return text

main()