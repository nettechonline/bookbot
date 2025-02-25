from stats import get_num_words, get_character_count, sort_stats
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    


    words = get_book_text(sys.argv[1])
    num_words = get_num_words(words)
    character_count = get_character_count(words)
    sorted_stats = sort_stats(character_count)

    # Report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in sorted_stats:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
        


if __name__ == '__main__':
    main()
