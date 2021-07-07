num = int(input())
hundreds = int(num / 100)
decimals = int(num / 10) % 10
last = num % 10
print(hundreds + decimals + last)
