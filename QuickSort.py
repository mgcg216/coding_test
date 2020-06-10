

# def quickSort(arr):
#     p = len(arr) - 1
#     passcounter = 0
#     for i in range(p):
#         if arr[i] > arr[p]:
#             arr[p-1], arr[p] = arr[p], arr[p-1]
#             arr[i], arr[p] = arr[p], arr[i]
#             p = p - 1
#         else:
#             passcounter = passcounter + 1
#         if i >= p:
#             break
#         if passcounter + 1 == p:
#             return(arr)
#     print(arr)
#     partition(arr[p], arr[0:p], arr[p+1:len(arr)])
#
# def partition(mid, lowarr, higharr):
#     print("low", lowarr)
#     print("high", higharr)
#     final = [quickSort(lowarr) + mid + quickSort(higharr)]
#     print(final)
#     return final

def quickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1
    if (low < high):
        pi = partition(arr, low, high)
        quickSort(arr, low, pi -1)
        quickSort(arr, pi + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [1, 2, 5, 4, -1, -2, 3]
done = quickSort(arr)
print(done)