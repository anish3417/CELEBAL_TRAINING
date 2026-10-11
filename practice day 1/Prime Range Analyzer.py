a = int(input())
b = int(input())
prime_count=0

for i in range(a,b+1):
    if (i<2):
        continue

    is_prime = True
    for j in range(2,i):
         if (i%j==0):
            is_prime = False
            break

    if is_prime:
        print(i)
        prime_count += 1

print(prime_count)
