star,space=1,3

for i in range(0,4):
    for j in range(0,space):
        print(" ",end=" ")
    for j in range(0,star):
        if(j%2==0):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
    space-=1
    star+=2
