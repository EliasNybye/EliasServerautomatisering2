with open("powerful.txt", "w") as file:
    file.write("python is powerful but sometimes tricky")                       
with open("powerful.txt", "r") as file:
    content = file.read()
    print(content)              
from collections import Counter

t = Counter(content)
print(t)

def count_repititions(string, t):
    return string.count(t)
def main():
    lettercheck = input("Enter a letter to check how often it appears in the text: ")
    repeatnumber = count_repititions(content, lettercheck)
    print(f"The letter '{lettercheck}' appears {repeatnumber} times in the text.")
if __name__ == "__main__":
    main()  

txt = "python"

x = txt.replace("python", "PYTHON", 1)
print(x)

