# https://morsecode.world/international/timing.html
MORSE_TO_GCODE_DICT = {
    '.': "M300 S550 P60",
    '-': "M300 S550 P180"
}

MORSE_INTERCHAR_GCODE = "M300 S0 P180"

MORSE_INTRACHAR_GCODE = "M300 S0 P60"

MORSE_INTERWORD_GCODE = "M300 S0 P420"

EN_TO_MORSE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '\'': '.----.',
    '"': '.-..-.'
}

'''
NOTE: this is definitely not the best way to do this
technically these are n^2 but we're still only ever going over each letter/symbol once
just breaking the string into chunks in order to avoid hanging spaces/silence and optimize GCODE
'''


def en_to_morse(str_en):
    str_morse = []
    for word in str_en.split(' '):
        word_morse = []
        for letter in word:
            if letter.upper() in EN_TO_MORSE_DICT:
                word_morse.append(EN_TO_MORSE_DICT[letter.upper()])
            else:
                print(f'WARNING: {letter} not in Morse code dictionary; omitting...')
        str_morse.append(' '.join(word_morse))
    return ' / '.join(str_morse)


def morse_to_gcode(str_morse):
    word_GCODE = []
    for word in str_morse.split(' / '):
        letter_GCODE = []
        for morse_letter in word.split(' '):
            symbol_GCODE = []
            for symbol in morse_letter:
                symbol_GCODE.append(MORSE_TO_GCODE_DICT[symbol])
            letter_GCODE.append(f'\n{MORSE_INTRACHAR_GCODE}\n'.join(symbol_GCODE))
        word_GCODE.append(f'\n{MORSE_INTERCHAR_GCODE}\n'.join(letter_GCODE))
    return f'\n{MORSE_INTERWORD_GCODE}\n'.join(word_GCODE)


# Driver
print("CTRL+C to exit")
while True:
    in_str = input('text: ').upper()
    morse = en_to_morse(in_str)
    print(morse)
    print(morse_to_gcode(morse))
