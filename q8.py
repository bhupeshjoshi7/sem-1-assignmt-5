# for i in range(0,3):
#     num =int(input("Enter the number "))
#     num1=[]
#     num1.append(num)
# print(num1))
list1=list(map(int,input("Enter the numbers separated by space:").split()))
for e in list1:
    if e>0:
        print(e,end=",")
print(" are positive numbers")  
for e in list1:
    if e<0:
        print(e,end=",")
print(" are negative numbers")        
for e in list1:
    if e%2==1:
        print(e,end=",")
print(" are odd numbers")  
for e in list1:
    if e%2==0:
        print(e,end=",")
print(" are even numbers")  
      


