st=input("enter string:")

c=0
t=True
for i in range(len(st)-1,0,-1):
    if(st[i]!=st[c]):
        t=False
        break
    c+=1

if(t):
    print("string is palindrome")
else:
    print("string is not palindrome")