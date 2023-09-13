import base64
import urllib.parse
from typing import List
import readchar

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(text):
    return base64.b64decode(text.encode()).decode()

def encode_hex(text):
    return text.encode().hex()

def decode_hex(text):
    return bytes.fromhex(text).decode()

def encode_binary(text):
    binary_string = ' '.join(format(ord(char), '08b') for char in text)
    return binary_string

def decode_binary(text):
    binary_values = text.split()
    decoded_text = ''.join([chr(int(val, 2)) for val in binary_values])
    return decoded_text

def decode_morse(text):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '/': ' '
    }

    morse_code_values = text.split()
    decoded_text = ''.join([morse_code_dict.get(val, val) for val in morse_code_values])
    return decoded_text

def encode_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }

    text = text.upper()
    encoded_text = ' '.join([morse_code_dict.get(char, char) for char in text])
    return encoded_text

def encode_url(text):
    return urllib.parse.quote(text)

def decode_url(text):
    return urllib.parse.unquote(text)

def select(
        options: List[str],
        selected_index: int = 0) -> int:
    print('\n' * (len(options) - 1))
    while True:
        print(f'\033[{len(options) + 1}A')
        for i, option in enumerate(options):
            print('\033[K{}{}'.format(
                '\033[1m[\033[32;1m x \033[0;1m]\033[0m ' if i == selected_index else
                '\033[1m[   ]\033[0m ', option))
        keypress = readchar.readkey()
        if keypress == readchar.key.UP:
            new_index = selected_index
            while new_index > 0:
                new_index -= 1
                selected_index = new_index
                break
        elif keypress == readchar.key.DOWN:
            new_index = selected_index
            while new_index < len(options) - 1:
                new_index += 1
                selected_index = new_index
                break
        elif keypress == readchar.key.ENTER or keypress == '\n':
            break
        elif keypress == readchar.key.CTRL_C:
            raise KeyboardInterrupt
    return selected_index

def main():
    while True:
        options = [
            "Base64 Encoding",
            "Base64 Decoding",
            "Hexadecimal Encoding",
            "Hexadecimal Decoding",
            "Binary Encoding",
            "Binary Decoding",
            "Morse Code Encoding",
            "Morse Code Decoding",
            "URL Encoding",
            "URL Decoding",
            "Exit"
        ]

        print("\nSelect an option:")
        selected_index = select(options)

        if selected_index == 0:
            text = input("Enter text to encode in Base64: ")
            result = encode_base64(text)
            print(f"Base64 Encoded: {result}")
        elif selected_index == 1:
            text = input("Enter Base64-encoded text to decode: ")
            result = decode_base64(text)
            print(f"Decoded Text: {result}")
        elif selected_index == 2:
            text = input("Enter text to encode in hexadecimal: ")
            result = encode_hex(text)
            print(f"Hexadecimal Encoded: {result}")
        elif selected_index == 3:
            text = input("Enter hexadecimal-encoded text to decode: ")
            result = decode_hex(text)
            print(f"Decoded Text: {result}")
        elif selected_index == 4:
            text = input("Enter text to encode in binary: ")
            result = encode_binary(text)
            print(f"Binary Encoded: {result}")
        elif selected_index == 5:
            text = input("Enter binary-encoded text to decode (space-separated): ")
            result = decode_binary(text)
            print(f"Decoded Text: {result}")
        elif selected_index == 6:
            text = input("Enter text to encode in Morse code: ")
            result = encode_morse(text)
            print(f"Morse Code: {result}")
        elif selected_index == 7:
            text = input("Enter Morse code to decode: ")
            result = decode_morse(text)
            print(f"Decoded Text: {result}")
        elif selected_index == 8:
            text = input("Enter text to URL encode: ")
            result = encode_url(text)
            print(f"URL Encoded: {result}")
        elif selected_index == 9:
            text = input("Enter URL-encoded text to decode: ")
            result = decode_url(text)
            print(f"Decoded Text: {result}")
        elif selected_index == 10:
            break

if __name__ == "__main__":
    main()
