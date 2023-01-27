str="ABCDEFGHIJKLMNO"
inc_str = str*100
for i in range(6):
    for j in range(i+1):
        print(inc_str[j:j])
    print()    
