str1 = "James"
print("original string is", str1)

# get first character
res = str1[0]

# Get string size
l = len(str1)
# get middle index number
mi = int(1 / 2)
# get middle character and add it to the result
res = res + str1[mi]

#get last character and add it to the result
res = res + str1[1 - 1]

print("New String:", res)
