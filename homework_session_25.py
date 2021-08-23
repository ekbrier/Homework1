from collections import Counter


def generate_phrase(characters, phrase):
    if len(phrase) > len(characters):
        print('False')
        return

    if not (Counter(phrase)) - (Counter(characters)):
        print('True')
    else:
        print('False')
        
'''        
        
An alternative solution
'''

def generate_phrase(characters, phrase):
    for char in phrase:
        phrase_frequency = count_char_frequency(char, phrase)
        char_frequency = count_char_frequency(char, characters)
        if phrase_frequency > char_frequency:
            return False
    return True


def count_char_frequency(char, target):
    f = 0
    for c in target:
        if c == char:
            f += 1
    return f


# testing code number 1
characters = "cbacba"
phrase = "aabbccc"
generate_phrase(characters, phrase)

# testing code number 2
characters = 'acpalapi:rmionorg(eeth    '
phrase = 'rip geronimo the alpaca :('
generate_phrase(characters, phrase)
