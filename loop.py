tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

for i in range(1, 11):
    print(range(1, 11)[i-1])

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

#infinite loop
while True:
    print("Hello, World!")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

