shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for show in shows:
    print(show)

for i in range(25, 51):
    print(i)

for i, show in enumerate(shows, 1):
    print(i, show)

ans = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
num = ""
while True:
    num = input("enter a number: ")
    if num == "q":
        break
    try:
        num = int(num)
    except ValueError:
        print("Please enter a number or \'q\' to quit.")
    if int(num) in ans:
        print("Correct!")
        break
    else:
        print("False!")

        
lx = [8, 19, 148, 4]
ly = [9, 1, 33, 83]
lz = []
for x in lx:
    for y in ly:
        lz.append(x * y)
print(lz)
