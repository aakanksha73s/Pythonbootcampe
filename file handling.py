# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a second line.\n')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write('This line is appended.\n')

# Reading lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')