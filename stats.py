def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)


def get_char_count(book_text):
    char_dic = {}
    for c in book_text:
        c = c.lower()
        
        if c not in char_dic:
            char_dic[c] = 1
        else:
            char_dic[c] += 1
            
    return char_dic
        