with open ("sample.txt", 'r') as file:
    line = file.readline()
    while line != '':
        print(line, end='')  # The 'end=''' prevents extra newline characters
        line = file.readline()
    

         