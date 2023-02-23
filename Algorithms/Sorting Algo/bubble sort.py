def bubble_sort(array_):
    indexing_length = range(0, len(array_) - 1)
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for i in indexing_length:
            if array_[i] > array_[i+1]:
                sorted_ = False
                array_[i], array_[i+1] = array_[i+1], array_[i]
    return array_

list_ = [27, 58, 5, 10, 17, 9, 87, 72, 15, 50, 24, 91, 70, 26, 80]
sorted_list = bubble_sort(list_)

print(sorted_list)



