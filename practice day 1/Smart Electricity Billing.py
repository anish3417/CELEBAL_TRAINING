
unit = int(input())

if (unit <=100):
    bal = unit*3

elif (unit <=200):
    bal = (100*3)+((unit-100) * 5)

else:
    bal = (100*3)+(100*5)+((unit-200)*8)

if(unit>300):
    bal += (bal*0.10)
print(bal)