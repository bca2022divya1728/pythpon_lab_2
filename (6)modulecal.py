def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b !=0:
        return a/b
    else:
        return "division by zero is not allowed"
    
def percentage(total,part):
    if total !=0:
        return(part/total)* 100
    else:
        return "total can't be zero"
    
import calculator
a=10
b=5
print(f"addition of {a} and {b}: {calculator.add(a,b)}")
print(f"subtraction of {b} and {a}: {calculator.subtract(a,b)}")
print(f"multiplication of {a} and {b}: {calculator.multiply(a,b)}")
print(f"division of {a} by {b}: {calculator.divide(a,b)}")
print(f"percentage of {b}and{a}: {calculator.percentage(a,b)}")


        