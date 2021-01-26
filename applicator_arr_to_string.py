# convert 1, 2, 3, 4, 6, 7, 8, 10 to "0-3, 5-7, 9"
import itertools
arr = [1, 2, 3, 4, 6, 7, 8, 10]
arr[:] = [i - 1 for i in arr]

def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

arrs = list(ranges(arr))

out = ""
for i in range(len(arrs)):
    if arrs[i][0] < arrs[i][1]:
        out = out + "{}-{}".format(str(arrs[i][0]), str(arrs[i][1]))
    elif arrs[i][0] == arrs[i][1]:
        out = out + str(arrs[i][0])
    else:
        print("Error")

    if i < len(arrs) - 1:
        out = out + ", "

print(out)
