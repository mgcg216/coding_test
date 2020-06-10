# 0, 1, 1, 2, 3, 5, 8, 13
# 0+1, 1+1, 1+3

def FibonacciNumbers(n):
    if n<0:
        print("Nope")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return FibonacciNumbers(n-1) + FibonacciNumbers(n-2)

print(FibonacciNumbers(9))