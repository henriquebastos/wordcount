from collections import Counter


def count(words):
    return Counter(words)


def asc(counter):
    return sorted(counter.items())


def top(counter, qty=20):
    return counter.most_common(qty)


def lines(counter):
    return '\n'.join(('{:10}: {:>4}'.format(w, c) for w, c in counter))
