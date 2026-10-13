a =input("Enter a number: ")

def check(a):
    i = len(a)
    for j in range(i):
        if a[j] != a[i-1]:
            return False
        else:

            i-=1

    return True



print(check(a))