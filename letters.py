LETTERS = {
    'a': 1,
    'A': 1,
    'b': 1,
    'B': 2,
    'D': 1,
    'd': 1,
    'e': 1,
    'g': 1,
    'o': 1,
    'O': 1,
    'p': 1,
    'P': 1,
    'q': 1,
    'Q': 1,
    'R': 1,
}


def num_buracos(word):
    """Sum number of wholes in word."""
    return sum([
        LETTERS.get(l, 0) for l in word
    ])


if __name__ == '__main__':
    print(num_buracos('Banana'))
    print(num_buracos('olho'))
    print(num_buracos('çzt'))
