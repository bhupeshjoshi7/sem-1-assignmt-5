start = int(input("Enter the starting range :"))
end  = int(input("Enter the ending range :"))
a = int(input("Enter the number:"))
for i in range(start,end+1):
    if i%a==0:
        print(i,end=",")