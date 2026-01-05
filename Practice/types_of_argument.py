#positional argument

def add(a,b):
    return a+b

result = add(1,2)
print(result)

#default arguments

def substract(a,b=10):
    return a-b
result = substract(20)
print(result)

#non default argument should not follow default argument

#keyword or named argument does not matter in which order we pass arguments

def multiply(a,b=10,c=10):
    return a*b*c
result = multiply(1,c=2)
print(result)

#variable length argument *args *args is tuple

def addition(*args):
    return sum(args)
result = addition(1,2,3)
print(result)

#variable length keyword args **kwargs is dictionary

def func(**kwargs):print(kwargs)

func(x=10,y=20,z=30)
