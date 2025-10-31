st=input("enter string:")
li=list(st)
res=""
for i,k in enumerate(li):
    if k.isdigit():
        for _ in range(int(k)):
            res+=li[i-1]


print(res)
