

password = input("correct password: ")

for i in range(3):
    print(f"attempt{i+1}")
    a=input()
    if a == password:
        print("Acess Granted")
        break

