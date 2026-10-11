binary_number = input()
decimal_number = 0
power = 0


length = len(binary_number)
for i in range(length):

    digit = binary_number[length - 1 - i]

    if digit == '1':
        decimal_number = decimal_number + (2 ** power)
    power = power + 1

print(decimal_number)
