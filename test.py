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


def embed_message(container, message):
    result = ""
    index = 0
    for char in container:
        if char == ' ' and index < len(message):
            result += ' ' * (ord(message[index]) - 32)
            index += 1
        else:
            result += char
    return result


def extract_message(embedded_text):
    extracted_message = ""
    space_count = 0
    for char in embedded_text:
        if char == ' ':
            space_count += 1
        else:
            if space_count > 0:
                extracted_message += chr(space_count + 32)  # Convert back using ASCII
                space_count = 0
    return extracted_message.strip()


def main():
    with open('message.txt', 'r') as file:
        message = file.read().strip()
    encrypted_message = caesar_cipher(message, 3)

    with open('container.txt', 'r') as file:
        container = file.read()

    embedded_text = embed_message(container, encrypted_message)

    with open('result.txt', 'w') as file:
        file.write(embedded_text)

    extracted_message = extract_message(embedded_text)
    original_message = caesar_cipher(extracted_message, 3, encrypt=False)

    print("Original Message:", message)
    print("Decrypted Message:", original_message)


if __name__ == "__main__":
    main()
