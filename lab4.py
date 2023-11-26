import matplotlib.pyplot as plt

# Paths to the files uploaded by the user
container_path = 'C:\\Users\\parlethed\\PycharmProjects\\TZI_lab4\\container.txt'
result_path = 'C:\\Users\\parlethed\\PycharmProjects\\TZI_lab4\\result.txt'


# Function to count the spaces and tabs at the end of each line
def count_spaces_tabs(file_path):
    with open(file_path, 'r') as file:
        return [len(line) - len(line.rstrip(' \t')) for line in file]


# Count spaces and tabs in both files
container_spaces_tabs = count_spaces_tabs(container_path)
result_spaces_tabs = count_spaces_tabs(result_path)

# Create a plot
plt.figure(figsize=(12, 6))
plt.plot(container_spaces_tabs, label='Container File', marker='o')
plt.plot(result_spaces_tabs, label='Result File', marker='x')
plt.title('Comparison of End-of-Line Whitespace between Original and Steganographed Text')
plt.xlabel('Line Number')
plt.ylabel('Number of Spaces/Tabs at EOL')
plt.legend()
plt.grid(True)
plt.show()
