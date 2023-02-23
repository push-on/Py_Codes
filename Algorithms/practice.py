arr = [2, 3, 6, 6, 5]
print(arr)
arr.sort()
arr.reverse()
print(arr)

big = arr[1]
i = 0
while i < len(arr)-1:
    if arr[i] == arr[i+1]:
        i+=1
    if arr[i] > arr[i+1]:
        big = arr[i+1]
        break

print(big)