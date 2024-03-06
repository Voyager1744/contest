"""Миша и математика"""

n = int(input())
a = list(map(int, input().split()))

operators = []
flag = False

if a[0] % 2 == 0:
    res = 0
else:
    res = 1

for i in range(1, n):
    if res == 1 and a[i] % 2 == 0:
        operators.append('+')
        res = 1
    elif res == 1 and a[i] % 2 == 1:
        operators.append('x')
        res = 1
    elif res == 0 and a[i] % 2 == 0:
        operators.append('x')
        res = 0
    elif res == 0 and a[i] % 2 == 1:
        operators.append('+')
        res = 1

if res:
    for i in operators:
        print(i, end='')


"""
3
5 7 2

x+


2
4 -5

+


3
390029247 153996608 -918017777

+x

"""