def apply(word):
    # remove mark
    clean_word = remove_mark(word)
    if is_short(clean_word) == 1:
        return 0
    return clean_word


# remove marks ['.', '?', '!', ',', '-']
def remove_mark(word):
    marks = ['.', '?', '!', ',', '-']
    for m in marks:
        word = word.replace(m, '')
    return word


# return 1 if word is one of the mark
def is_mark(word):
    marks = ['.', '?', '!']
    for m in marks:
        if m == word:
            return 1
    return 0


# remove words that are too short
def is_short(word):
    if len(word) <= 1:
        return 1
    return 0


