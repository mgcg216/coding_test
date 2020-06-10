
def bubbleSort(arr):
    n = len(arr)
    passcounter = 0
    for i in range(n):
        j = i + 1
        print(arr)
        if j + 1 > n:
            if passcounter + 1 == n:
                print("done")
                print(arr)
                return
            else:
                bubbleSort(arr)
        else:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                passcounter = passcounter + 1


arr = [5, 1, 4, 2, 8]
bubbleSort(arr)


