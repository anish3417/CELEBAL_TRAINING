amount = float(input())

if amount >= 5000:
    payable_amount = amount - (amount * 0.20)  # 20% off
elif amount >= 3000:
    payable_amount = amount - (amount * 0.10)  # 10% off
elif amount >= 1000:
    payable_amount = amount - (amount * 0.05)  # 5% off
else:
    payable_amount = amount

print(int(payable_amount))
