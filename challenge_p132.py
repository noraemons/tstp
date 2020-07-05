with open("st.txt", "r") as f:
    print(f.read())
        
with open("q_and_a.txt", "w") as f:
    ans = input("What is your fav food?")
    f.write(ans)

with open("q_and_a.txt", "r") as f:
    print(f.read())


import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]
          ]
with open("movies.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for mov in movies:
        w.writerow(mov)

with open("movies.csv", "r") as f:
    print(f.read())
