morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '＄': '...-..-', '@': '.--.-.', ' ': '/'
}


def convert_to_morse(text, morse_dict):
    converted_text = ""
    for letter in text.upper():
        if letter in morse_dict:
            converted_text += morse_dict[letter]
        converted_text += " "
    return converted_text[:-1]


def convert_to_text(morse_code, morse_dict):
    list_of_codes = morse_code.split()
    converted_code = ""
    for code in list_of_codes:
        converted_code += list(morse_dict.keys()
                               )[list(morse_dict.values()).index(code)]
    return converted_code
