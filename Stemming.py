from nltk.stem import PorterStemmer

ps = PorterStemmer()


def apply_stemming(word):
    return ps.stem(word)


