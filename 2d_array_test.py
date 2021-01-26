arr = [[1.0, 2.0], [10.0, 11.0, 12.0], [6.0]]
compare = [1.0, 11, 10]

def tray_helper(arr, comp):
    """
    :param arr: 2d array of serials and tray that I will need to compare
    :param comp: unaccounted for serials
    :return:
    """
    hash = {}
    for i in range(len(comp)):
        hash[comp[i]] = i

    for i in range(len(arr)):
        sers = [] # unacounted for serial per tray
        for j in range(len(arr[i])):
            ser = arr[i][j]
            if ser in hash:
                sers.append(ser)
        if sers:
            print("In tray {} with {} items, the serials {} do not have a Final acceptance Log ".format(i+1, len(arr[i]), sers))


tray_helper(arr, compare)