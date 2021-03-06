# Merge Sort Array

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) <= 1: return list
    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)

list = [234,1, 3, 5, 2, 4, 6]
print(mergesort(list))

