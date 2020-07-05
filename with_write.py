with open("st.txt", "w") as f:
    f.write("Hi from Python!")
    
with open("st.txt", "r") as f:
    print(f.read())
