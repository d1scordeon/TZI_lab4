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
    words = container.split()
    result = []
    for i, word in enumerate(words):
        if i < len(message):
            result.append(word + message[i])
        else:
            result.append(word)
    return ' '.join(result)


def extract_message(embedded_text, message_length):
    words = embedded_text.split()
    extracted_message = ""
    for word in words[:message_length]:
        extracted_message += word[-1]
    return extracted_message


def main():
    # Read and encrypt the message
    with open('message.txt', 'r') as file:
        message = file.read().strip()
    encrypted_message = caesar_cipher(message, 3)

    # Read the container text
    with open('container.txt', 'r') as file:
        container = file.read()

    # Embed the message
    embedded_text = embed_message(container, encrypted_message)

    # Write the embedded text
    with open('result.txt', 'w') as file:
        file.write(embedded_text)

    # Extract and decrypt the message (for demonstration)
    extracted_message = extract_message(embedded_text, len(encrypted_message))
    original_message = caesar_cipher(extracted_message, 3, encrypt=False)

    print("Original Message:", message)
    print("Decrypted Message:", original_message)

if __name__ == "__main__":
    main()
