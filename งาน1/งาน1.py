max_num = 9
num = max_num
 
for i in range(max_num):
    for s in range(i):
        print(" ", end=' ')
 
    for n in range(1, num+1):
        print(n, end=' ')
 
    num -= 1
    print("")
