a = [4, 7, 2, 9, 5, 12, 15]   
b = [x for x in a if x > 5]
print(b)  

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)  
avg = calculate_average(b)
print(f"Average: {avg}") 

