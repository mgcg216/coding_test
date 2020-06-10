"""
Given an string in roman no format (s)  your task is to convert it to integer .

Input:
The first line of each test case contains the no of test cases T. Then T test cases follow. Each test case contains a string s denoting the roman no.

Output:
For each test case in a new line print the integer representation of roman number s.

Constraints:
1<=T<=100
1<=roman no range<4000

Example:
Input
2
V
III
Output
5
3
"""
#
# def RomanNumerals(n):
#     Roman = {
#         1: "I",
#         5: "V",
#         10: "X",
#         50: "L",
#         100: "C",
#         500: "D",
#         1000: "M"
#     }
#     print(Roman.get(n, "Invalid Digit"))

# RomanNumerals("V")

def RomanNumerals(n):
    Roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return Roman.get(n, -1)

def convertRtoI(string):
    total = 0
    past = -1
    repeat = 0
    for elem in string:
        curr = RomanNumerals(elem)
        print(repeat)
        if past > curr or past/curr < 0 or curr//past == 5 or curr//past == 1 and curr == past and repeat < 2:
            if curr/5 == past:
                total = total + curr - 2*past
            else:
                total = total + curr
                if past == curr:
                    repeat = repeat + 1
                else:
                    repeat = 0
            past = curr
        else:
            print("Invalid Roman Numeral")
            return
    print(string, " is ", total)


convertRtoI("XIII")
convertRtoI("XIV")
convertRtoI("XIX")
convertRtoI("XIIII")
convertRtoI("MXI")