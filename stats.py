def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1         
    return chars

def sort_on(dt):
    return dt["num"]

def dict_sort(dict):
    sorted= []
    for c in dict:
        sorted.append({"char": c, "num":dict[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted