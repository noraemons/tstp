def squared(x):
    return x * x

print(squared(5))

""

def print_string(x):
    print(x)

print_string("Hello")

""
      
def function1(x, y, z, n = 0, m = 0):
    return (x + y + z) / (n + m + 1)

print(function1(1, 2, 3, 4))

""

def fun1(x):
    return x / 2

def fun2(y):
    return y * 4

a = fun1(5)
b = fun2(a)

print(b)

""

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Invalid Input")

c = convert("3")
print(c)

""


    
