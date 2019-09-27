#Even Fibonacci numbers
#sum of Even Fibonacci numbers below 4'000'000
num1, num2 = 1, 2
myset = set()
while num2 < 4000000:
    myset.add(num2 if num2 % 2==0 else 0)
    num1, num2 = num2, num1+num2

print(sum(myset))
