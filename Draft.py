list = [27, 58, 5, 10, 17, 9, 87, 87, 4, 15, 50, 24, 87, 70, 2, 0]

n = 0
i_max = max(list)
for i in list:
    if i == i_max:
        n += 1

print(n)