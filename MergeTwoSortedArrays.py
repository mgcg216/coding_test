"""
Merge Two sorted array
"""


def bubbleSort(arr):
    while True:
        counter = 1
        for i in range(len(arr)):
            try:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    counter = counter + 1
            except IndexError:
                pass
        if counter >= len(arr):
            print(arr)
            return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while True:
            if j < 0 or key > arr[j]:
                break
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)
    return arr




arr1 = [8, 10, 3, 2, 1, 6]
arr2 = [6, 4, 5, 7, 9, 11]

arr1 = insertionSort(arr1)
# arr1 = bubbleSort(arr1)
arr2 = bubbleSort(arr2)

def mergeTwoSortedArrays(arr1, arr2):
    arr = [None] * (len(arr1) + len(arr2))
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
    print(arr)
    return arr

mergeTwoSortedArrays(arr1, arr2)
