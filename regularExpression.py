import re

string = "Two too."
m = re.findall("t[wo]o", string, re.IGNORECASE)
print(m)

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

found = re.findall("__.*__", t)
for match in found:
    print(match)