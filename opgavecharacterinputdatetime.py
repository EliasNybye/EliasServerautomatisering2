import datetime
current_year = datetime.datetime.now().year
name = input ("whats is your name? ")
age = int(input("How old are you? "))
print(f"{name}, you will be 100 years old in {current_year - age + 100}")   

