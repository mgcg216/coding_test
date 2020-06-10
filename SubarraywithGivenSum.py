"""
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is
 the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray
from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 10^7
1 <= Ai <= 10^10

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
"""

def subarraywithGivenSum(input):
    N = input[0][0]
    for i in range(N*2):
        if i % 2 == 1:
            sumCheck(input[i:i+2])


def sumCheck(simpleInput):
    """

    :param simpleInput:
    return:
    example
    1 2 3 7 5
    check
    1 2 3 7 5
    3 5 10 12
    6 12 15
    13 17
    18
    """
    N = simpleInput[0][0]
    S = simpleInput[0][1]
    step = N
    while True:
        if step < 0:
            break
        for i in range(step):
            sum = 0
            for j in range(N-step+1):
                sum += simpleInput[1][i+j]
            if sum == S:
                print(N-step+1, " ", i+1)
                step = -1
                break
        step -= 1


input = [[2], [5, 12], [1, 2, 3, 7, 5], [10, 15], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
subarraywithGivenSum(input)

# simpleInput = [[5, 12], [1, 2, 3, 7, 5]]
# sumCheck(simpleInput)
# simpleInput2 = [[10, 15], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# sumCheck(simpleInput2)