import sys

file = open(sys.argv[1])

summ = 0
count = 0
total = 0

s = file.readlines()
s = [line.rstrip() for line in s]

for i in s:
    summ += int(i)
    count += 1

average = summ / count

for i in s:
    total += abs(int(i) - int(average))

print(total)
file.close()
