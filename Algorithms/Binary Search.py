# binary search
pos = -1


def search(array_, key):
    l = 0
    u = len(array_) - 1
    while l <= u:
        mid = (l + u) // 2
        if array_[mid] == key:
            globals()["pos"] = mid
            return True
        else:
            if array_[mid] < key:
                l = mid + 1
            else:
                u = mid - 1
    return False


list_ = [2, 5, 8, 12, 16, 20, 38, 56, 72, 91]
key_ = 20

if search(list_, key_):
    print("found at ", pos + 1)
else:
    print("Not Found")
