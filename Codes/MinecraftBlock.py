import math

width = int(input("Enter width: "))
length = int(input("Enter length: "))
depth = int(input("Enter depth: "))

total_time_seconds = (width * length * depth) * 5

hours = math.floor(total_time_seconds / 3600)
total_time_seconds %= 3600
minutes = math.floor(total_time_seconds / 60)
seconds = total_time_seconds % 60

print("Steve will take %d hours %d minutes %d seconds." %(hours, minutes, seconds))