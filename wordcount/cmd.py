from wordcount.core import lines, asc, count, top


def count_words(words):
    return lines(asc(count(words)))


def top_words(words, qty=20):
    return lines(top(count(words), qty))


def read_words(fileobj):
    with fileobj as f:
        return f.read().lower().split()
