from stats import get_book_text, get_num_words, get_sorted_dic
import sys

if (len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found 75767 total words")
    print("--------- Character Count -------")
    sorted_dic = get_sorted_dic()
    for entry in sorted_dic:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")




main()
