author = "kafka"
print(author[0])
print(author[-1])

cat = "cat" + " in" + " the" + " hat"
print(cat,
      "cat" * 3,
      cat.upper(),
      cat.lower(),
      cat.capitalize()
      )

name = "William Faulkner"
print("Hello, {}".format(name))

year_born = "1897"
print("{} was born in {}.".format(name, year_born))

print(
    "I jumped over a puddle. It was 10 feet long!".split(".")
    )

first_three = "abc"
result = "+".join(first_three)
print(result)

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(words)
print(one)

s = "   The   "
s = s.strip()
print(s)

equ = "All animals are equal"
equ = equ.replace("a", "@")
print(equ)

print(
    "animals".index("m")
    )

print(
    "She said, \"yeah,\" at that time."
    )

print("line1\nline2\nline3")

"""Slice: starting index includes the numeber but the ending index doesn't"""
abc = ["a", "b", "c", "d", "e"]
print(
    abc[0:3]
    )



