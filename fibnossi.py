import sys
def findIndex(n):

    if (n < 0):
        return -1

    a = 0
    b = 1
    c = 1
    res = 1
    if n==0:
        print("Fibonacci number")
        return 1
    if n==1:
        print("Fibonacci number")
        return 2

    while (c < n):
        c = a + b

        # res keeps track of number of
        # generated fibonacci number
        res = res + 1
        a = b
        b = c
    if (c == n):
        print("Fibonacci number")
        return res
    print("ERROR:Not fibonacci")
    return -1


# Driver program to test above function
result = findIndex(int(sys.argv[1]))
print(result)