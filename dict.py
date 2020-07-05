my_dict = dict()
my_dict

facts = dict()
facts["code"] = "fun"

print(facts["code"])

print("code" in facts)

del facts["code"]
print("code" in facts)

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"
         }

n = input("Please enter a number: ")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("cannot find")


locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)
