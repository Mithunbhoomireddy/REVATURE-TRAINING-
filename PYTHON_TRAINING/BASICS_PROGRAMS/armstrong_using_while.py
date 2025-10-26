#while loop
number=int(input("enter a number: "))
temp=number
sum=0
pow = len(str(number))
while number>0:
     dig=number%10
     sum+=dig**pow
     number//=10
if sum==temp:
    print(temp," is armstrong")
else:
    print(temp," not armstrong")

#for loop
val=int(input("enter a number: "))
sum1=0

for i in range(1,val+1):
   sum1+=i
print(sum1)

animals=['cat','dog','rabbit','elephant']
s1='mithun'
s2=[10,20,30,40,50]
s3=[]
#for each loop
for i in animals:
    print(i)
for i in s1:
    print(i)
for i in s2:
    s3.append(i*i)
print(s3)