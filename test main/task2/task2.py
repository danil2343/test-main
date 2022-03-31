import sys

center = open(sys.argv[1])
points = open(sys.argv[2])

ab = float(center.read(1))
cb = float(center.read(2))
d = float(center.read(3))


def PointInCircle(ab, cb, d, a, c):
    result = ((a - ab) ** 2 + (c - cb) ** 2) ** 0.5
    if result < d:
        print('1')
    elif result > d:
        print('2')
    else:
        print('0')


p = points.readlines()
for i in p:
    a = float(i[0])
    c = float(i[2])
    PointInCircle(ab, cb, d, a, c)
center.close()
points.close()

