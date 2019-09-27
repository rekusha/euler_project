#Multiples of 3 and 5
#sum of Multiples of 3 and 5 below 1000
myset = set()
count = 0

while True:
    if count * 3 < 1000:
        myset.add(count * 3)
    if count * 5 < 1000:
        myset.add(count * 5)
    if count * 3 >= 1000:
        break
    count += 1

print(sum(myset))
