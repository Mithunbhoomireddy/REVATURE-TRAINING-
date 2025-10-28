"""
date-27-10-2025
"""
#while loop
NUMBER=int(input("enter a number: "))
TEMP=NUMBER
SUM=0
POW = len(str(NUMBER))
while NUMBER>0:
    dig=NUMBER%10
    SUM+=dig**POW
    NUMBER//=10
if SUM==TEMP:
    print(TEMP," is armstrong")
else:
    print(TEMP," not armstrong")

#for loop
VAL=int(input("enter a number: "))
SUM1=0

for i in range(1,VAL+1):
    SUM1+=i
print(SUM1)

ANIMALS=['cat','dog','rabbit','elephant']
S1='mithun'
S2=[10,20,30,40,50]
S3=[]

#for each loop
for i in ANIMALS:
    print(i)

for i in S1:
    print(i)

for i in S2:
    S3.append(i*i)
print(S3)
