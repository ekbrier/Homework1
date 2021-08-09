from collections import Counter


def generate_phrase(characters, phrase):
    character_list = list(characters)
    phrase_list = list(phrase)

    if len(characters) < len(phrase):
        print('False')
        return

    if not (Counter(phrase_list)) - (Counter(character_list)):
        print('True')
    else:
        print('False')


# testing code number 1
characters = "cbacba"
phrase = "aabbccc"
generate_phrase(characters, phrase)

# testing code number 2
characters = 'acpalapi:rmionorg(eeth    '
phrase = 'rip geronimo the alpaca :('
generate_phrase(characters, phrase)
