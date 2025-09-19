def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower_case_text = text.lower()
    char_count = {}
    for char in lower_case_text:
        char_count[char] = char_count.get(char,0)+1
    return char_count