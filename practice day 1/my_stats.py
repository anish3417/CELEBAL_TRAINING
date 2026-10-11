def mean(numbers):
    return sum(numbers) / len(numbers)

def variance(numbers):
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)

def std_deviation(numbers):
    return variance(numbers) ** 0.5
