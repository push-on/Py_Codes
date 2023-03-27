# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to
# left diagonal = 3 + 5 + 9 = 17. Their absolute
# difference is |15 - 17 | = 2. solve it using python

def difference(arr):
    d1 = 0
    d2 = 0
    n = len(arr)

    for i in range(len(arr)):
        for j in range(0, n):
            if (i == j):
                d1 += arr[i][j]
            if (i == n - j - 1):
                d2 += arr[i][j]
    return abs(d1 - d2)

arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]

print(difference(arr))
