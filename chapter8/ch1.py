import statistics

numbers = [23, 234, 73, 4593, 12, 1]

median_h = statistics.median_high(numbers)
median = statistics.median(numbers)
median_low = statistics.median_low(numbers)

print(median_h)
print(median)
print(median_low)