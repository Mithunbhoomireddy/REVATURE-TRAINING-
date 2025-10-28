# iterator itr(),next()
"""
date-27-10-2025
"""
STR1='HELLO'
li=iter(STR1)
print(next(li))
print(next(li))
print(next(li))
print(next(li))
print(next(li))

def answer(s):
    char_count = {}
    for char in s:
       if char in char_count:
           char_count[char] +=1
       else:
           char_count[char] = 1
    for char in s:
            if char_count[char] ==1:
                return char
    return "null"
s=input('Enter a string: ')
result=answer(s)
print(result)
