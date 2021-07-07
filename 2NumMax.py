a = int(input())
b = int(input())
first = a // b
second = b // a
anb = (a * first + b * second) // (first + second)
# even = first * (a // b) * (b // a)
print(anb)
