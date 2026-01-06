try:
    with open("sample.txt", 'r') as file:
        for line in file:
            print(line, end='') # The 'end=''' prevents extra newline characters
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")