import sys
def get_book_text():
    with open(sys.argv[1], 'r') as f:
        return f.read()

def get_num_words():
    book_words = get_book_text().split()
    return len(book_words)

def get_num_each_character():
    dic = {}
    for character in get_book_text():
        if (character.lower() in dic):
            dic[character.lower()] += 1
        else:
            dic[character.lower()] = 1

    return dic

def get_sorted_dic():
    dic = get_num_each_character()
    dic_list = [{"char": k, "num": v} for k,v in dic.items() if k.isalpha()]
    dic_list.sort(key=lambda x: x["num"], reverse = True)
    return dic_list
