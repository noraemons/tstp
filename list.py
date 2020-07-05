fruit = ["Apple", "Orange", "Pear"]
print(fruit)

fruit.append("Banana")
fruit.append("Peach")
print(fruit)

a = fruit.pop()
b = fruit.pop()

print(a, b, fruit)

double_fruit = fruit + fruit
print(double_fruit)

print("Apple" in double_fruit)

len(double_fruit)

colors = ["purple", "orange", "green"]
guess = input("what is the color? (input):")
if guess in colors:
    print("Correct!")
else:
    print("Incorrect! Try again!")

