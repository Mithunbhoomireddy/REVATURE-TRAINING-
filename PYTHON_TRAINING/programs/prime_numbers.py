num=input("Enter a number: ")
def prime(num):
    start = 1
    for i in range(1,num+1):
        ran(start)
        start += 1
def ran(num):
    count=0
    for i in num:
        if(num%i==0):
            count+=1
    if(count==2):
        print(num)
prime(num)

