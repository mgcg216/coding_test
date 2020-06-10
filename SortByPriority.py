
priority = (5, 1, 3, 2)
input = [1, 7, 5, 8, 2]

# hash = [0]*len(priority)
# print('The hash is:', hash(priority))
maximum = max(input)
hash = [0]*(maximum+1)
print(hash)

def insert(val):
    n = len(val)
    for i in range(0, n):
        hash[val[i]] = 1


insert(input)
print(hash)


def sortByPriority(input_hash, priority):
    arr = []
    for i in range(0, len(priority)):
        if input_hash[priority[i]] == 1:
            arr.append(priority[i])
            input_hash[priority[i]] = 0
    print(input_hash)
    for j in range(len(input_hash)):
        if input_hash[j] == 1:
            arr.append(j)
    print(arr)

sortByPriority(hash, priority)