

def bubbleSort(arr):
    count = 1
    for i in range(len(arr)):
        try:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                count += 1
        except IndexError:
            pass
    if count >= len(arr):
        print(arr)
        return arr
    bubbleSort(arr)

arr = [5, 1, 4, 2, 8]
arr2 = [11, 8, 64, 6, 5, 12, 1, 4, 2, 8, 9, 10]
bubbleSort(arr2)