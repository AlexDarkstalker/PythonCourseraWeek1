height = int(input())
perDay = int(input())
perNight = int(input())
print((height - perNight - 1) // (perDay - perNight) + 1)
