def add(a,b):
    result=a+b
    return result,10,20
a=int(input("enter first number"))
b=int(input("enter second number"))
c=add(a,b)

#positional parameters
print(add(a,b))

#keyword arguments
def person(name, age):
    print(name, age)

person(age=22, name="Mithun")

# arbitory arguments
def sum(*value):
    sum=0
    for item in value:
        sum+=item
    return sum
print(sum(10,20,30,40))

#keyword arbitory arguments
def voter(**details):
    return f"voter name: {details['name']}  age: {details['age']} voter id :{details['id']}"

print(voter(id=20213432,age=20,name="Mithun"))

#optional arguments
e=10
f=20
g=30
h=40
def add(e,f,g=0,h=0):
    result=e+f+g+h
    print(result)
add(e,f)
add(e,f,g)
add(e,f,g,h)

#return multiple values
x=2
y=3
z=4
def calculate(x,y,z):
    total=x+y+z
    average=total/3
    return total,average
tot,av=calculate(x,y,z)
print(tot,"\n",av)

#anonimous/lamda function
college=lambda name,rollno,marks: f"name:{name},rollno:{rollno},marks:{marks}"
print(college("Mithun",3,921))
