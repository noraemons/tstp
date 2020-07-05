import re

text = 'The ghost that says boo haunts the loo'

def find_oo(text):
    a = re.findall(".oo", text)
    print(a)

find_oo(text)