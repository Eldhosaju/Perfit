arr = []
lim = int(input("Enter the limit"))
for i in range(0, lim):
    eleme = int(input("Enter the values"))
    arr.append(eleme)
lngth = len(arr)
for i in range(lim-1):
    for j in range(0, lim-1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
print ("Sorted array is:")
for i in range(lngth):
    print("%d" %arr[i])