import matplotlib.pyplot as plt


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


def embed_message(container_path, message, result_path):
    with open(container_path, 'r') as container_file:
        container_lines = container_file.readlines()

    encrypted_message = caesar_cipher(message, 3)
    message_index = 0

    with open(result_path, 'w') as result_file:
        for line in container_lines:
            if message_index < len(encrypted_message):
                spaces_to_add = ord(encrypted_message[message_index]) - 32
                result_file.write(line.rstrip() + ' ' * spaces_to_add + '\n')
                message_index += 1
            else:
                result_file.write(line)


def extract_message(file_path, message_length):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    extracted_message = ""
    for line in lines[:message_length]:
        extracted_message += chr(len(line) - len(line.rstrip()) + 32)

    return caesar_cipher(extracted_message, 3, encrypt=False)


def count_spaces_tabs(file_path):
    with open(file_path, 'r') as file:
        return [len(line) - len(line.rstrip(' \t')) for line in file]


# Specify the paths
container_path = 'C:\\Users\\parlethed\\PycharmProjects\\TZI_lab4\\container.txt'
result_path = 'C:\\Users\\parlethed\\PycharmProjects\\TZI_lab4\\result.txt'
message_path = 'C:\\Users\\parlethed\\PycharmProjects\\TZI_lab4\\message.txt'

# Read the message
with open(message_path, 'r') as message_file:
    message = message_file.read().strip()

# Embed the message
embed_message(container_path, message, result_path)

# Extract the message for verification (optional)
extracted_message = extract_message(result_path, len(message))
print("Extracted Message:", extracted_message)

# Visualization
container_spaces_tabs = count_spaces_tabs(container_path)
result_spaces_tabs = count_spaces_tabs(result_path)

plt.figure(figsize=(12, 6))
plt.plot(container_spaces_tabs, label='Container File', marker='o')
plt.plot(result_spaces_tabs, label='Result File', marker='x')
plt.title('Comparison of End-of-Line Whitespace between Original and Steganographed Text')
plt.xlabel('Line Number')
plt.ylabel('Number of Spaces/Tabs at EOL')
plt.legend()
plt.grid(True)
plt.show()
