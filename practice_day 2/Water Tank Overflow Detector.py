numbers = list(map(int,input().split()))
print(numbers)

mint=0
cap=0

for n in numbers:
    cap += n
    mint+=1
    if(cap>1000):
        print(mint)
        break
