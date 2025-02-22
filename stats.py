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

def sort_stats(character_count):
    character_count_lst = []

    for k,v in character_count.items():
        character_count_lst.append({k:v})
    
    return character_count_lst