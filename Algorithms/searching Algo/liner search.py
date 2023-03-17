list_1 = (10, 20, 80, 30, 60, 50, 110, 100, 130, 170)
i = None
key = int(input("number: "))
result = None
for i in range(len(list_1)):
    if key == list_1[i]:
        result = list_1[i]
        break

if result == key:
    print("found at", i)
else:
    print("not found")
