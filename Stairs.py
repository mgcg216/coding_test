"""
Given a stair of size N and two ways to reach next step, take 1 step at a time or two steps at at time. What is the
total possible ways you can reach staircase of particular length
"""

from itertools import combinations_with_replacement
from itertools import permutations

def stairs(steps, movements):
    countermin = 0
    countermax = 0
    minmov = steps
    maxmov = steps
    while True:
        minmov = minmov - min(movements)
        maxmov = maxmov - max(movements)
        if minmov < 0:
            countermax = countermax + 1
            countermin = countermin + 1
            break
        countermin = countermin + 1
        if maxmov > 0:
            countermax = countermax + 1
    comb = []
    for x in range(countermax, countermin):
        temp = list(combinations_with_replacement(movements, x))
        comb.append(temp)
    out = []
    for x in list(comb):
        for i in list(x):
            if sum(i) == steps:
                perm = list(set(permutations(i)))
                out.append(perm)
    print(out)




# def combinations(movements, length, max, out=[]):
#     movements.sort() # Sort to get the LSB to MSB
#     out = [0]*max
#     if length >= 1:
#         for x in range(max):
#             out[(len(movements)-length)] = movements[length]
#             combinations(movements, length - 1, max, out)
#     else:
#         print(out)
#         return

# def combinations(movements):
#     movements.sort()
#     out = [0] * 5
#     for i in range(len(movements)):
#         for x in range(5):
#             out[x] = movements[i]
#             print(out)
#
# combinations([2, 1, 3])
#

stairs(13, [1,2, 3, 4])