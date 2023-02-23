def selection_sort(array_):
    for i in range(len(array_)):
        min_in = i
        for j in range(i + 1, len(array_)):
            if array_[min_in] > array_[j]:
                min_in = j
        array_[min_in], array_[i] = array_[i], array_[min_in]
    return array_


list_ = [27, 58, 5, 10, 17, 9, 87, 72, 15, 50, 24, 91, 70, 26, 80]
sorted_list = selection_sort(list_)
print(sorted_list)
