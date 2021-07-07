a = int(input())
b = int(input())
n = (a % b)
k = (n + b - 1) // b
print(k * "NO", 0**k * "YES", sep="")
