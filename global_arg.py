x = 100

def f(y=10, z=20):
    global x
    x += 1
    print(x + y + z)

f(5)
