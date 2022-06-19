# def hello(name,age):
#     year=2022-age
#     print(f"hello {name},your were born in {year}")

# def hello(name,age):
#     year=2022-age
#     print("welcome to akirachix")
#     return
#     print(f"hello {name},your were born in {year}")

    # positional arg
# def hello(name,age):
#     year=2022-age
#     print("welcome to akirachix")
#     return f"hello {name},your were born in {year}"

# default arg
# def my_country(country="Uganda",student="suzan"):
#     return f"Hello {student} you are from {country}"

# Afuction that accepts any number of positional arguments.
# def greet_multiple(*names):
#     # print(names)
#     for name in names:
#         print(f"hello {name}")
        
def my_sum(*numbers):
    sum=0
    for number in numbers:
        sum+=number
        return sum
    
    # A function that accepts any number of the keyword arguments
def greet_multiple(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    
def greet(**kwargs):
    keys=kwargs.keys()   
    if "country" in keys:
        print(f"Hello {kwargs['name']} you are from {kwargs['country']}")
    elif "age" in keys:
        year=2022-kwargs['age']
        print(f"Hello {kwargs['name']} you were born in {year}")
    elif not kwargs:
        print(f"hello anonimous")    
        
        
def sum_greet(*args,**kwargs):
    sum=0
    for num in args:
        sum+=num
        keys=kwargs.keys()
    if "name" in keys:
        print(f"hello {kwargs['name']} the answer is {sum}")
    elif "country" in keys:
        print(f"hello {kwargs['name']} from {kwargs['country']},the answer is {sum}")
    elif not keys:
        print(f"hello anonimous the answer is {sum}")