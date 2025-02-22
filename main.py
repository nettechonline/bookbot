from stats import get_num_words, get_character_count, sort_stats

def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def main():
    words = get_book_text()
    num_words = get_num_words(words)
    character_count = get_character_count(words)
    sorted_stats = sort_stats(character_count)
    print(sorted_stats)



    # Report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for _ in sorted_stats:
        for key, value in sort_stats.items():
            if key.isalpha():
                print(f"{key}: {value}")

    print("============= END ===============")
        


if __name__ == '__main__':
    main()
