num = int(input())
first = num // 1000
second = num // 100 % 10
third = num // 10 % 10
fourth = num % 10
difference = (first * 1000 + second * 100 + third * 10 + fourth) \
             - (fourth * 1000 + third * 100 + second * 10 + first)
print((difference**2 + 1))
# print(((first - fourth) ** 2 + (second - third) ** 2 + 1) % 10)
