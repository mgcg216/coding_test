# def makeRegistrar():
#     registry = {}
#
#     def registrar(func):
#         registry[func.__name__] = func
#         return func  # normally a decorator returns a wrapped function,
#                   # but here we return func unmodified, after registering it
#     registrar.all = registry
#     return registrar
#
# reg = makeRegistrar()
# @reg
# def f1(a):
#     return a+1
#
# @reg
# def f2(a, b):
#     return a+b
#
# print(reg.all)
# print(reg.all(['f1']))

def arrFunc(*args):

    def function_picker(x):
        def f1():
            print('hello')

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

    def f4(num):
        print(num)

    for u in args:
        function_picker(u)




# arrFunc([1, 3, 2, [4, "Four"]])
arrFunc(1)