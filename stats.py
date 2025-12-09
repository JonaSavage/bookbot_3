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



def sort_on(char_dict):
    return char_dict["count"]
    
    
def sorted_char_count(char_dict):
    list_char_dicts = []
    for i in char_dict:
        if not i.isalpha():
            continue
        
        temp = {
            "char": i,
            "count": char_dict[i],
            
        }
        list_char_dicts.append(temp)
    
    list_char_dicts.sort(reverse=True, key=sort_on)
    return list_char_dicts
        