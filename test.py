def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text += chr(int(byte, 2))
    return text


def embed_message(container, binary_message):
    result = ""
    index = 0
    for char in container:
        if char == ' ' and index < len(binary_message):
            result += ' ' if binary_message[index] == '0' else '  '
            index += 1
        else:
            result += char
    return result


def extract_message(embedded_text):
    binary_message = ""
    i = 0
    while i < len(embedded_text):
        if embedded_text[i] == ' ':
            if i + 1 < len(embedded_text) and embedded_text[i + 1] == ' ':
                binary_message += '1'
                i += 2
            else:
                binary_message += '0'
                i += 1
        else:
            i += 1
    return binary_message


def main():
    with open('message.txt', 'r') as file:
        message = file.read().strip()
    encrypted_message = caesar_cipher(message, 3)

    binary_message = text_to_binary(encrypted_message)

    with open('container.txt', 'r') as file:
        container = file.read()

    embedded_text = embed_message(container, binary_message)

    with open('result.txt', 'w') as file:
        file.write(embedded_text)

    extracted_binary = extract_message(embedded_text)
    decrypted_message = binary_to_text(extracted_binary)
    original_message = caesar_cipher(decrypted_message, 3, encrypt=False)

    print("Original Message:", message)
    print("Decrypted Message:", original_message)


if __name__ == "__main__":
    main()
