import string

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if "a" in i:
        newlist.append(i)
print(newlist)

#List comprehension syntax: [expression for i in iterable if condition]

newlist = [i for i in fruits if "a" in i]
print(newlist)

language = 'Python'
list = [i for i in language]
print(list)

#Generating
numbers = [i for i in range(10)]
print(numbers)

#Math operations
squares = [i**2 for i in range(10)]
print(squares)

#Tuples
numbers = [(i,i**2) for i in range(10)]
print(numbers)

#with if expression

even_numbers = [i for i in range(23) if i%2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(23) if i%2 != 0]
print(odd_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_numbers = [i for i in numbers if i >0]
print(positive_numbers)

negative_numbers = [i for i in numbers if i < 0]
print(negative_numbers)

positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

#Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

#def
def sum(a, b):
    return a + b
print(sum(7,8))

#lambda
# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))

x = lambda firstElement, secondElement : firstElement + secondElement
print(x(7, 8))

def complex_sum(sum, a, b):
    return sum(a, b) * 2

print(complex_sum(x, 2, 2))

cube = lambda x: x **3
print(cube(4))

multiple_variables = lambda a, b, c: a**2 - 3*b + 4*c
print(multiple_variables(5, 5, 3))

#lambda function inside another function

def power(x):
    return lambda n: x ** n

cube = power (2) (3)
print(cube)

two_power_five = power (2) (5)
print(two_power_five)



