x = 0
k = 0
res = []
while k<999//2:
    if (999-k) * (999 - x) == int(str((999-k) * (999 - x))[-1::-1]):
        res.append((999-k) * (999 - x))
    if x > 999//2:
        x = 0
        k += 1
    x+=1
print(max(res))
