numMinutes = int(input())
finalMins = numMinutes % 60
hours = int(numMinutes / 60) % 24
print(hours, finalMins)
