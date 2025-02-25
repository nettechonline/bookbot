def get_num_words(text_to_count):
    return len(text_to_count.split())

def get_character_count(text_to_count):
    character_count = {}
    for _ in text_to_count.lower():
        if _ in character_count:
            character_count[_] += 1
        else:
            character_count[_] = 1
    return character_count


def sort_on(d):
    return d["num"]


def sort_stats(character_count):
    sorted_list = []

    for i in character_count:
        sorted_list.append({"char": i, "num": character_count[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list