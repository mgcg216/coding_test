import numpy as np

def iterConverter(num, sbearr):
    """
    To have a for loop like method iterators are needed. For example
    for i in range(2)
        for j in range(4)
            for k in range(4)
    will have the iteraotrs in list form where the MSD is at the start and LSB at the end.
    :param num: Value that is being tracked
    :param sbearr: array of the ranges for the loop
    :return: array of iterators
    """
    if num >= np.prod(sbearr):
        raise ValueError("num is greater than the product of sbearr")
    temp = 1
    returnarr = np.array([], dtype=np.int)
    for a in sbearr:
        temp = temp * a
        arrvalue, num = divmod(num, np.prod(sbearr) / temp)
        returnarr = np.append(returnarr, arrvalue)
    returnarr = returnarr.astype(int)
    return returnarr

"""
for i in range(10):
    print(i)
"""
i = 0
while i != 8:
    print(i, iterConverter(i, [3, 2, 2]))
    i += 1