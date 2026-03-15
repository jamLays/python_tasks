# def generate_full_name():
#     first_name = input('Enter your first name: ')
#     last_name = input('Enter your last name: ')
#     full_name = first_name + ' ' + last_name
#     print(full_name)
# generate_full_name()
from datetime import datetime


# def add_2_numbers():
#     first_number = int(input('Enter your first number: '))
#     second_number = int(input('Enter your second number: '))
#     add_number = first_number + second_number
#     print(add_number)
# add_2_numbers()

#Using Return
# def generate_full_name():
#     first_name = input('Enter your first name: ')
#     last_name = input('Enter your last name: ')
#     full_name = first_name + ' ' + last_name
#     return full_name
# print(generate_full_name())


def greetings(name):
    message = name +','+ ' ' + 'Welcome to Python'
    return message

print(greetings('Jim'))

def add_ten(num):
    ten = 10
    add_ten = num + ten
    return add_ten

print(add_ten(30))

def square(x):
    return x ** 2

print(square(5))

def area_of_circle(r):
    PI = 3.14
    return PI * r**2

print(area_of_circle(7))

def sum_of_squares(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

print(sum_of_squares(10))

# def generate_full_name (first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name
# print('Full_name:', generate_full_name(input('First name: '), input('Last name: ')))
#
# def sum_of_2_numbers(num1, num2):
#     sum = num1 + num2
#     return sum
#
# num1 = int(input('First number: '))
# num2 = int(input('Second number: '))
# print('sum_of_2_numbers:', sum_of_2_numbers(num1, num2))

# def calculate_age(current_year, birth_year):
#     age = current_year - birth_year
#     return age
# print('calculate_age:', calculate_age(2026, 1999))

# def weight_of_object (mass, gravity):
#     weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
#     return weight
#
# mass = int(input('Mass: '))
# gravity = 9.81
# print('weight_of_object:', weight_of_object(mass, gravity))

#Returning value
def print_name(firstname):
    return firstname
print_name('Asabeneh')
print(print_name('Asabeneh'))


# def is_even (num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# num = int(input('Enter a number: '))
# print(is_even(num))


# def find_even_numbers(n):
#     even_numbers = []
#     for i in range(n+1):
#         if i % 2 != 0:
#             even_numbers.append(i)
#     return even_numbers
# print(find_even_numbers(15))

#is_even=True - even, False - odd
# def find_even_numbers(total, is_even):
#     found_numbers = []
#
#     for current_number in range(total + 1):
#         if (current_number % 2 == 0 and is_even == True) or (current_number % 2 != 0 and is_even == False):
#             found_numbers.append(current_number)
#
#     return found_numbers
#
# print(find_even_numbers(10,True))


def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Lays'))


def generate_full_name(firstname = 'Leysa', lastname = 'Yami'):
    full_name = firstname + ' ' + lastname
    return full_name
print(generate_full_name())
print(generate_full_name('David', 'Semi'))

def calculate_age(birthday = 1999, years = 2026):
    age = years - birthday
    return age
print(calculate_age())
print(calculate_age(1989,2026))

def sum_of_num(*nums):
    total =0
    for num in nums:
        total = total + num
    return total
print(sum_of_num(5, 10, 21, 43))

def generate_group(team, *args):
    print(team,':')
    for i in args:
        print(i)

print(generate_group('Team-1', 'Lays', 'An', 'Max'))

def greet(name, location):
    print('Hello', name, 'welcome to', location)
greet ('Leysan', 'Moscow')


my_dict = {
    'name': 'Leysan',
    'location': 'Bali',

}

greet(**my_dict)

def square(n):
    return n ** 2
def do_smth(f,x):
    return f(x)
print(do_smth(square, 10))











