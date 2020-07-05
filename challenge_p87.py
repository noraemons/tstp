musicians = ["BUMP OF CHICKEN", "SILENT SIREN", "Houkago Tea Time"]
print(musicians)

locations = {"Tokyo": (38.000, 135.000), "Gunma": (39.000, 135.000)}
print(locations)

myself = {"height": "180cm", "weight": "75kg", "nationality": "Japan"}
print(myself)

getkey = input("What do you want to know about me: ")
if getkey in myself:
    print(myself[getkey])
else:
    print("no info")

musiclist = ["Snow Smile", "Fujiyama Disco", "Fuwafuwa Time"]

music_combi = {}
for i in range(3):
    music_combi[musicians[i]] = musiclist[i]
    
print(music_combi)
