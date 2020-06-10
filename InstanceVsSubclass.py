""" Undertstanding instance vs subclass"""

class MainClass:
    pass

class ChildClass(MainClass):
    pass

class GrandChildClass(ChildClass):
    pass

child = ChildClass()

print(isinstance(child, MainClass))
print(issubclass(ChildClass, MainClass))
print(isinstance(child, ChildClass))
print(issubclass(ChildClass, ChildClass))
print(isinstance(child, GrandChildClass))
print(issubclass(ChildClass, GrandChildClass))