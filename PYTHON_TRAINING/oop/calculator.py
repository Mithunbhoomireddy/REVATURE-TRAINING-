from ArithmeticCalculations import  ArithmeticCalculations
from AgeNotSufficientToVoteError import AgeNotSufficientToVoteError
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
age=int(input("enter the age:"))
calc=ArithmeticCalculations(n1,n2)

print(calc.add())
print(calc.sub())
print(calc.mul())

try:
    if n2==0:
        raise ZeroDivisionError("number 2 is zero")
    if age<18:
        raise AgeNotSufficientToVoteError("you are not eligible to vote")
except ZeroDivisionError as e:
    print(e)
except AgeNotSufficientToVoteError as e:
    print(e)
else:
    try:
        l1 = [1, 5, 7, 3]
        val = l1[10]
        res = calc.div()
        print(res)
    except ZeroDivisionError:
        print(",don't give zero as denominator")
    except IndexError as err:
        print(f"{err},index out of bounds")
    except:
        print("something went wrong")
    else:
        print("no error")
    finally:
        print("operation completed")

