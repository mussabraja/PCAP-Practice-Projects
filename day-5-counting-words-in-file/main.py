import string

def count_occurences(file_name, word):
    with open(file_name) as file:
        text = file.read()
    words = text.lower().split()
    clean_words = [w.strip(string.punctuation) for w in words]   # nishan hatao
    return clean_words.count(word.lower())
