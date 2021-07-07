numSeconds = int(input())
secondsFirst = numSeconds % 60 // 10
secondsSecond = numSeconds % 60 % 10
minutesFirst = numSeconds // 60 % 60 // 10
minutesSecond = numSeconds // 60 % 60 % 10
hours = numSeconds // 3600 % 24
print(hours, str(minutesFirst) + str(minutesSecond),
      str(secondsFirst) + str(secondsSecond), sep=":")
