import math
n = int(input("Enter the number"))
if n % 2 == 0:
    print(2)
    n = n/2

for i in range(3, int(math.sqrt(n))+1):
    if n % i == 0:
        print(i)
        n = n/i