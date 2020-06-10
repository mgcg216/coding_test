"""
Printing an array into Zigzag fashion is discussed here. Suppose you were given an array of integers, and you are told
to sort the integers in a ‘zig-zag’ pattern. In general, in a zig-zag pattern, the first integer is less than the second
 integer, which is greater than the third integer, which is less than the fourth integer, and so on. Hence, the
 converted array should be in the form of e1 < e2 > e3 < e4 > e5 < e6.
"""

# Brought in my bubble sort
def zigZag(arr):
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
                zigZag(arr)
        else:
            if i % 2 == 0:
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    passcounter = passcounter + 1
            else:
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    passcounter = passcounter + 1


arr=[4, 3, 7, 8, 6, 2, 1]
zigZag(arr)