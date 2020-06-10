"""
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. T testcases follow. Each case contains a string S containing characters.

Output:
For each test case, in a new line, output a single line containing the reversed String.

Constraints:
1 <= T <= 100
1 <= |S| <= 2000

Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr
"""

def reverseString(str):
    s = 0
    e = 0

    for i in range(len(str)):
        # if i == len(str) - 1:
        #     print(str[i])
        if str[i] == "." or i == len(str) - 1:
            if i == len(str)-1:
                e = i + 1
            else:
                e = i
            print(str[s:e])
            if s < e:
                while e >= s:
                    print(str[e])
                    e = e - 1
            else:
                print(e)
            s = i + 1

    # s = pass #i = len(str) - 1
    # while i >= e: #0:
    #     print(str[i])
    #     i = i - 1

str1 = "i.like.this.program.very.much"
reverseString(str1)