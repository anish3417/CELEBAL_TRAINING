def is_armstrong_string(number):
    num_str = str(number)
    num_digits = len(num_str)


    total_sum = sum(int(digit) ** num_digits for digit in num_str)

    return total_sum == number



print(is_armstrong_string(1634))
print(is_armstrong_string(123))
