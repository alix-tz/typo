import random

NEIGHBORING_LETTERS = {
    'a': ['z', 'q'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'e': ['r', 'd', 's', 'z'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['f', 't', 'y', 'h', 'b', 'v'],
    'h': ['n', 'b', 'g', 'y', 'u', 'j'],
    'i': ['o', 'k', 'j', 'u'],
    'j': ['h', 'u', 'i', 'k', 'n'],# ','],
    'k': ['j', 'i', 'o', 'l'],# ';', ','],
    'l': ['k', 'o', 'p', 'm'],#, ';', ':'],
    'm': ['l', 'p', 'ù'], #, ':', '!'],
    'n': ['b', 'h', 'j', 'k'],#, ','], 
    'o': ['i', 'k', 'l', 'p'],
    'p': ['o', 'l', 'm', 'ù'],
    'q': ['a', 'w', 'z', 's'],
    'r': ['e', 'd', 'f', 't'],
    's': ['a', 'z', 'e', 'd', 'x', 'w', 'q'],
    't': ['r', 'f', 'g', 'y'],
    'u': ['y', 'h', 'j', 'i'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 's', 'x'],
    'x': ['w', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 'q', 's', 'e'],
    # CUSTOM CAPITAL LETTERS
    'A': ['Z', 'Q', '1'],
    'B': ['V', 'G', 'H', 'N'],
    'C': ['X', 'D', 'F', 'V'],
    'D': ['S', 'E', 'R', 'F', 'C', 'X'],
    'E': ['R', 'D', 'S', 'Z', '3', '4'],
    'F': ['D', 'R', 'T', 'G', 'V', 'C'],
    'G': ['F', 'T', 'Y', 'H', 'B', 'V'],
    'H': ['N', 'B', 'G', 'Y', 'U', 'J'],
    'I': ['O', 'K', 'J', 'U', '8', '9'],
    'J': ['H', 'U', 'I', 'K', 'N'],# ','],
    'K': ['J', 'I', 'O', 'L'],# ';', ','],
    'L': ['K', 'O', 'P', 'M'],#, ';', ':'],
    'M': ['L', 'P', 'ù'], #, ':', '!'],
    'N': ['B', 'H', 'J', 'K'],#, ','],
    'O': ['I', 'K', 'L', 'P', '9', '0'],
    'P': ['O', 'L', 'M', '%', '0', '°'],
    'Q': ['A', 'W', 'Z', 'S'],
    'R': ['E', 'D', 'F', 'T', '4', '5'],
    'S': ['A', 'Z', 'E', 'D', 'X', 'W', 'Q'],
    'T': ['R', 'F', 'G', 'Y', '5', '6'],
    'U': ['Y', 'H', 'J', 'I'],
    'V': ['C', 'F', 'G', 'B', '7', '8'],
    'W': ['Q', 'S', 'X'],
    'X': ['W', 'S', 'D', 'C'],
    'Y': ['T', 'G', 'H', 'U', '6', '7'],
    'Z': ['A', 'Q', 'S', 'E', '2', '3'],
    # CUSTOM SPECIAL CHARS
    #'&': ['é', '²'],
    #'é': ['"', '&'],
    #"'": ['"', '('],
    #'(' : ["'", '-'],
    #'-' : ['(', 'è'],
    #'è' : ['-', '_'],
    #'_' : ['è', 'ç'],
    #'ç' : ['_', 'à'],
    #'à' : ['ç', ')'],
    #')' : ['à', '='],
    #'=' : [')', '$'],
    #'^' : ['¨', '$'],
    #'$' : ['^', '*'],
    #'*' : ['$', 'ù'],
    # CUSTOM ALT GR
    # todo
}

NEIGHBORING_NUMPAD_DIGITS = {
    '0': ['1', '2'],
    '1': ['4', '5', '2', '0'],
    '2': ['0', '1', '4', '5', '6', '3'],
    '3': ['2', '5', '6'],
    '4': ['7', '8', '5', '2', '1'],
    '5': ['7', '8', '9', '4', '6', '1', '2', '3'],
    '6': ['9', '8', '5', '2', '3'],
    '7': ['8', '5', '4'],
    '8': ['7', '4', '5', '6', '9'],
    '9': ['8', '5', '6']
}

NEIGHBORING_DIGITS = { # using AZERTY keyboard layout
    '1': ['2', '&', '³'],
    '2': ['1', '3', 'é'],
    '3': ['2', '4', '"'],
    '4': ['3', '5', "'"],
    '5': ['4', '6', '('],
    '6': ['5', '7', '-'],
    '7': ['6', '8', 'è'],
    '8': ['7', '9', '_'],
    '9': ['8', '0', 'ç'],
    '0': ['9', 'à', '°'],
}


VISUALLY_SIMILAR_DIGITS = {
    '0': ['6', '8', '9'],
    '1': ['7'],
    '2': ['7'],
    '3': ['5', '8', '9'],
    '4': ['9'],
    '5': ['3', '8'],
    '6': ['0', '8'],
    '7': ['1', '2'],
    '8': ['0', '3', '5', '6'],
    '9': ['0', '3', '4']
}

VISUALLY_SIMILAR_CHARS = { # customized to visually similar handwritten chars
    '0': ['6', '8', '9', 'o', 'D', 'O', 'U'],
    '1': ['7', 'I'],
    '2': ['7', 'Q', 'Z'],
    '3': ['5', '8', '9'],
    '4': ['9', 'U', 'A'],
    '5': ['3', '8', 'S', '9', '7'],
    '6': ['0', '8', 'b', 'G'],
    '7': ['1', '2', 'T', 'Z'],
    '8': ['0', '3', '5', '6', 'B', 'S'],
    '9': ['0', '3', '4', 'g', 'q', '5'],
    'a': ['e', 'o'],
    'b': ['6', 'd', 'p'],
    'c': ['e', 't', ],
    'e': ['c', 'i', 'a', 'o', 'r', 's', 't'],
    'g': ['9', 'q', 'j', 'p', 'z'],
    'i': ['I', 'l', 'j', 'u', 'e', 'r', 't', 'y'],
    'm': ['n', 'ui', 'ni', 'in', 'iu', 'rn', 'im', 'ri', 'rm', 'nu'],
    'n': ['m', 'u', 'ui', 'iu', 'ri', 'ni', 'in'],
    'o': ['e', 'a', '0', 'O', 'er'],
    'p': ['q', 'b', 'g', 'd'],
    'q': ['9', 'g', 'p'],
    'r': ['n', 'v', 's'],
    's': ['t', 'e', 'r', 'z'],
    't': ['c', 'e', 'r', 's', 'f'],
    'u': ['v', 'n', 'ii', 'ui', 'iu', 'in', 'ni', 'ur', 'ru'],
    'v': ['u'],
    'y': ['z'],
    'z': ['y'],
    'B': ['8', 'P'],
    'C': ['G'],
    'D': ['0', 'O'],
    'E': ['F'],
    'F': ['7', 'E', 'R'],
    'G': ['6', 'C'],
    'I': ['1', 'i', 'L', 'T'],
    'L': ['I'],
    'M': ['N'],
    'N': ['M'],
    'O': ['0', 'D', 'U'],
    'P': ['B'],
    'Q': ['2'],
    'S': ['5', '8'],
    'T': ['I', '7'],
    'U': ['0', '4', 'O', 'V'],
    'V': ['U', 'W'],
    'W': ['U'],
    'X': ['Y'],
    'Y': ['5', 'X'],
    'Z': ['2', '7'],
    # CUSTOM ACCENTUATED CHARS
    'é': ['e', 'è', 'ê', 'ë'],
    'è': ['é', 'ê', 'ë', 'e'],
    'ê': ['é', 'è', 'ë', 'e'],
    'ë': ['é', 'è', 'ê', 'e'],
    'à': ['a', 'â', 'ä'],
    'â': ['a', 'à', 'ä'],
    'ä': ['a', 'à', 'â'],
    'ù': ['u', 'û', 'ü'],
    'û': ['u', 'ù', 'ü'],
    'ü': ['u', 'ù', 'û'],
    'ô': ['o', 'ö'],
    'ö': ['o', 'ô'],
    'ç': ['c'],
    'î': ['i', 'ï'],
    'ï': ['i', 'î'],
    'É': ['E', 'È', 'Ê', 'Ë'],
    'È': ['É', 'Ê', 'Ë', 'E'],
    'Ê': ['É', 'È', 'Ë', 'E'],
    'Ë': ['É', 'È', 'Ê', 'E'],
    'À': ['A', 'Â', 'Ä'],
    'Â': ['A', 'À', 'Ä'],
    'Ä': ['A', 'À', 'Â'],
    'Ù': ['U', 'Û', 'Ü'],
    'Û': ['U', 'Ù', 'Ü'],
    'Ü': ['U', 'Ù', 'Û'],
    'Ô': ['O', 'Ö'],
    'Ö': ['O', 'Ô'],
    'Ç': ['C'],
    'Î': ['I', 'Ï'],
    'Ï': ['I', 'Î'],
    # VISUALLY SIMILAR PUNCT (or close enough)
    '.': [',', '!', '?', ';', ':'],
    ',': ['.', '!', '?', ';', ':'],
    '!': ['.', ',', '?', ';', ':'],
    '?': ['.', ',', '!', ';', ':'],
    ';': ['.', ',', '!', '?', ':'],
    ':': ['.', ',', '!', '?', ';'],
    '(': [')', '[', ']', '{', '}'],
    ')': ['(', '[', ']', '{', '}'],
    '[': [']', '(', ')', '{', '}'],
    ']': ['[', '(', ')', '{', '}'],
    '{': ['}', '(', ')', '[', ']'],
    '}': ['{', '(', ')', '[', ']'],
    '<': ['>'],
    '>': ['<']
}


# Data type classes, and capitalization are preserved. #custom: sort of!
def get_random_neighbor(char, seed=None):
    if seed is not None:
        random.seed(seed)

    if len(char) != 1:
        raise Exception("Need exactly one character to find a neighbor")

    if char.isdecimal():
        numpad = random.choice([True, False])
        if numpad:
            return random.choice(NEIGHBORING_NUMPAD_DIGITS[char])
        else:
            return random.choice(NEIGHBORING_DIGITS[char])
    elif char in NEIGHBORING_LETTERS:
        neighbor = random.choice(NEIGHBORING_LETTERS[char])
        return neighbor
    else:
        return char


def get_random_visually_similar_char(char, seed=None):
    if seed is not None:
        random.seed(seed)

    if len(char) != 1:
        raise Exception("Need exactly one character to find a visually similar character")

    if char in VISUALLY_SIMILAR_CHARS:
        return random.choice((VISUALLY_SIMILAR_CHARS[char]))
    else:
        return char


def get_random_visually_similar_digit(char, seed=None):
    if seed is not None:
        random.seed(seed)

    if len(char) != 1:
        raise Exception("Need exactly one character to find a visually similar digit")

    if char.isdigit():
        if char in VISUALLY_SIMILAR_DIGITS:
            return random.choice((VISUALLY_SIMILAR_DIGITS[char]))
        else:
            return char
    else:
        raise Exception("'" + char + "' is not a digit.")
