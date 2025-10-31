st=input("enter string:")
c=0
vo={'a','e','i','o','u','A','E','I','O','U'}

for i in range(len(st)):
    if(st[i] in vo):
        c+=1

print("count of vowels in string:",c)