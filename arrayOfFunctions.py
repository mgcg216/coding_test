

def arrFunc(arr=None):
    if arr is None:
        arr = []

    # def f1():
    #     print(1)
    #
    # def f2():
    #     print(2)
    #
    # def f3():
    #     print(3)

    # arr = [f1, f3, f2]
    def function_picker(x):
        def f1():
            print(1)

        def f2():
            print(2)

        def f3():
            print(3)

        def f4(num):
            print(num)

        switcher = {
            1: f1,
            2: f2,
            3: f3,
            4: f4
        }
        func = switcher.get(x, lambda: "Invalid")
        func()

    # function_picker(1)
    for i in range(len(arr)):
        function_picker(arr[i])




arrFunc([1, 3, 2, 4])
