def add(a,b):
    answer=a+b
    return answer

def subtract(a,b):
    answer=a-b
    return answer

def multiply(a,b):
    answer=a*b
    return answer
def divide(a,b):
    answer=a/b
    return answer

def exponet(a,b):
    answer=a**b
    return answer
def modulus(a,b):
    answer=a%b
    return answer
def square(a,b):
    answer=a**2
    return answer
def cube(a,b):
    answer=a**3
    return answer
def intdivide(a,b):
    answer=a//b
    return answer

def factors(a):
    x=1
    for i in range(1,a+1):
        x*=i
    return x
