x = [3,5,8,3,5,6,7,2,1,4,9,0]
x.append(3)
my_list = [3,5,"KingKong", [8,3,5]]
for element in my_list:
    print(element)
for i in range(len(x)):
    if x[i] < 10:
        print(x[i]) 
for i in x:
    if i < 10:
        print(i)
