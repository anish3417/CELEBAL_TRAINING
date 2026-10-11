

print(" enter balance")
balance  = int(input())

print("how much want to withdraw")

b= int(input())


if balance < b or b % 100 != 0:

        print("failed")
else:
      balance-=b
      print("SUCCESS")


