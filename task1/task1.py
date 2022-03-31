import sys

n = sys.argv [1]
m= sys.argv [2]

p = [i for i in range(1, int(n)+1)]
listResult = [1]
while True:
    for i in range(0, int(m)-1):
        p.append(p.pop(0))
    if p[0] == 1 :
        break
    else :
        listResult.append(p[0])
print(*listResult)
