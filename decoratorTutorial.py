
# Assigning Functions to Variables
def plus_one(numbers):
    return numbers + 1

add_one = plus_one
print(add_one(5))

# Defining Functions Inside other Functions
def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result

print(plus_one(4))

# Passing FUnctions as Arguments to other functions
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))

# Functions Returning other Functions
def hello_function():
        def say_hi():
            return "Hi"
        return say_hi()
hello = hello_function()
print(hello)

# Nested Functions have access to Enclosing Function's Variable Scope
def print_message(message):
    # print("enclosing Function")
    def message_sender():
        # print("Nested Function")
        print(message)
    message_sender()


print_message("Random Message")

# Creating Decorator

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def say_hi():
    return "hello there"

decorate = uppercase_decorator(say_hi)
print(decorate())

# Python Easier decorator
@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()

# Applying Multiple Decorators to a Single Function
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

# Accepting Arguments in Decorator Function
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are : {0}, {1}.".format(arg1, arg2))
        function(arg1, arg2)
    return  wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Northridge", "Chatsworth")

#Defining General Purpose Decorators
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1, 2, 3)