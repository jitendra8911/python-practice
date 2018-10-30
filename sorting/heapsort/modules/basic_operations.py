from math import floor


def parent(i):
    if i % 2 == 0:
        return i / 2 - 1
    else:
        return floor(i / 2)


def left(i):
    return 2 * i + 1


def right(i):
    return (2 * i) + 2
