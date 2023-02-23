list_ = [27, 58, 5, 10, 17, 9, 87, 4, 15, 50, 24, 3, 70, 2, 0]

smallest_number = list_[0]

for i in range(len(list_)-1):

    item = list_[i]

    if smallest_number > list_[i]:
        smallest_number = list_[i]

print(smallest_number)
