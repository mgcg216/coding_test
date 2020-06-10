

# def bubbleSort(arr):
#     passcount = 1
#     for i in range(len(arr)):
#         try:
#             if arr[i+1] < arr[i]:
#                 arr[i + 1], arr[i] = arr[i], arr[i+1]
#             else:
#                 passcount += 1
#         except IndexError:
#             pass
#     if passcount >= len(arr) - 3:
#         print(arr)
#         return arr
#     else:
#         bubbleSort(arr)




# def bubbleSort(arr):
#     counter = 1
#     for i in range(len(arr)):
#         try:
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#             else: counter += 1
#         except IndexError:
#             pass
#     if counter >= len(arr):
#         print(arr)
#         return arr
#     else: bubbleSort(arr)


def bubbleSort(arr):
    while True:
        counter = 1
        for i in range(len(arr)):
            try:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                else: counter += 1
            except IndexError: pass
        if counter >= len(arr):
            print(arr)
            return arr













arr = [5, 1, 4, 2, 8]
arr2 = [11, 8, 64, 6, 5, 12, 1, 4, 2, 8, 9, 10]
bubbleSort(arr2)
