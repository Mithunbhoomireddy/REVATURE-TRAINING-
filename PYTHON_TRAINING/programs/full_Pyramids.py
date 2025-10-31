star,space=1,2

for i in range(0,3):
    for j in range(0,space):
        print(" ",end=" ")
    for j in range(0,star):
        print("*",end=" ")
    print()
    space-=1
    star+=2
