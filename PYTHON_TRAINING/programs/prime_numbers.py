# num=input("Enter a number: ")
# def prime(num):
#     start = 1
#     for i in range(1,num+1):
#         ran(start)
#         start += 1
# def ran(num):
#     count=0
#     for i in num:
#         if(num%i==0):
#             count+=1
#     if(count==2):
#         print(num)
# prime(num)

# #largest of 3 numbers
# a,b,c=map(int,input().split())
# print(f"largest of 3 numbers:{max(a,b,c)}")

# # factorial of a given number
# num=int(input("Enter a number: "))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

# fibbonacci series for the given no. of numbers
# num=int(input("Enter a number: "))
# a,b=0,1
# for _ in range(num):
#     print(a)
#     a,b=b,a+b

#
# for i in range(1,4):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
for i in range(a,b+1):
    count=0
    for j in range(1,i+i):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i)


