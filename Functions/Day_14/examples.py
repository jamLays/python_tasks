from functools import reduce

#1. Function as a Parameter

def sum_numbers(numbers):
    return sum(numbers)

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)

#2. Function as a Return Value

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_func(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_func('square')
print(result(5))

result = higher_order_func('cube')
print(result(5))

result = higher_order_func('absolute')
print(result(-5))

#3. Python Closures

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

result = add_ten()
print(result(10))

#Creating Decorators
# Normal function

def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper
result = uppercase_decorator(greeting)
print(result())

@uppercase_decorator
def greeting():
    return 'Welcome to Python'
result = greeting()
print(result)
#By placing @uppercase_decorator directly above the function definition, the function greeting is being "decorated" with
# the uppercase_decorator function.

#The function uppercase_decorator is the decorator.

#The function greeting is the function that gets decorated.


#Applying Multiple Decorators to a Single Function
#First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

def string_split_decorator(function):
    def wrapper():
        func = function()
        return func.split()
    return wrapper

@string_split_decorator
@uppercase_decorator
#order with decorators is important in this case - .upper() function does not work with lists

def greeting():
    return 'Welcome to Python'

print(greeting())

#Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function (para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach".format(first_name, last_name))

print_full_name("John", "Smith", "USA")

#Map Function
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_square = map(square, numbers)
print(list(numbers_square))

#The same with a lambda function
numbers_squared = map(lambda x: x **2, numbers)
print(list(numbers_squared))

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def change_upper(name):
    return name.upper()
names_upper = map(change_upper, names)
print(list(names_upper))

names_upper = map(lambda name: name.upper(), names)
print(list(names_upper))

#Filter Function

numbers = [1, 2, 3, 4, 5]
def even_numbers(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(even_numbers, numbers)
print(list(even_numbers))

def odd_numbers(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(odd_numbers, numbers)
print(list(odd_numbers))

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))

#Reduce Function
numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)









