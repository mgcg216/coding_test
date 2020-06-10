"""
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 10^5
1 <= A[i] <= 10^6

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

Explanation:
Testcase 1: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5

"""

input = [[2], [4], [1, 5, 3, 2], [3], [3, 2, 7]]
simpleInput = [[4], [1, 5, 3, 2]]

def bubbleSort(arr):
    while True:
        count = 0
        for i in range(len(arr)):
            try:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    count += 1
            except IndexError:
                pass
        if count >= len(arr) - 1:
            print(arr)
            return arr


bubbleSort(simpleInput[1])
simpleInput = [[4], [1, 5, 2, 3]]

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        print('i ', i)
        while True:
            # print(arr[i], " ", arr[j])
            if j < 0:
                break
            if arr[i] < arr[j]:
                for k in range(i-j):
                    arr[k] = arr[k+1]
                    print(j+k)
            print('j ', j)
            j -= 1
    print(arr)
    return arr

insertionSort(simpleInput[1])
# simpleInput = [[4], [1, 5, 3, 2]]
#
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return
#     L = arr[0:len(arr)//2]
#     R = arr[len(arr)//2:len(arr)]
#     print(L)
#     print(R)
#     mergeSort(L)
#     mergeSort(R)
# print(simpleInput[1])
# mergeSort(simpleInput[1])
