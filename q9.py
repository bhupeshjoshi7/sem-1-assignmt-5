str = input("Enter the string  :")

list=[]
count =0
list=str.split(" ")
print(list)
for e in list:
    for j in list:
        if e==j:
            count=count+1
    print(count)        
print(count)        