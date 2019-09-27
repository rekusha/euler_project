#Largest prime factor
#Largest prime factor for 600851475143
from math import sqrt
n = int(sqrt(600851475143))
a = list(range(n+1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1

while 600851475143 % lst[-1] != 0:
    lst.pop()

print(lst[-1])
