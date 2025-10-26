'''
Date:25-10-2-2-25
DES: biggest of 2 no.
'''
from unittest import case

a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
    print(f" greatest nubmer :",a)
    print(f'{a:.2f} is bigger then {b:.4f}')
elif a==b:
    print("both are equal ")
else:
    print(" greatest number :",b)
    print(f'{b:2f} is bigger then {a:5f}')
#ternary operator
print(f'it is very{'expensive' if a>b else'cheap'}')

#match case

weeknumber=int(input("enter a week number: "))
match weeknumber:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case _:
        print("enter a valid week number between 1 and 6")

