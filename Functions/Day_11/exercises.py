import math
# 1.Declare a function add_two_numbers. It takes two parameters and it returns a sum
from contextlib import nullcontext


def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(10, 35))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle

def area_of_circle(radius):
    import math
    area = math.pi * radius ** 2
    return area
final = area_of_circle(5)
print (round(final, 2))

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments
# Check if all the list items are number types. If not do give a reasonable feedback

def add_all_nums(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum
print(add_all_nums(10, 35,55))

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit

def convert_C_to_F(C):
    fahrenheit = (C * (9 / 5)) + 32
    return fahrenheit
print(convert_C_to_F(100))

#5. Write a function called check-season, it takes a month parameter and returns
# the season: Autumn, Winter, Spring or Summer
def check_season(month):
    if month =='January' or month == 'February' or month == 'December':
        return 'Winter'
    if month == 'March' or month == 'April' or month == 'May':
        return 'Spring'
    if month == 'June' or month == 'July' or month == 'August':
        return 'Summer'
    if month == 'September' or month == 'October' or month == 'November':
        return 'Autumn'
print(check_season('April'))

#6.Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(m,b,x):
    y = m * x + b
    return y
print(calculate_slope(2,5,0.5))

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn

def linear_eqn (b,c):
    x1 = x2 = -c/b
    return x1, x2

def solve_quadratic_eqn (a, b, c):
    if a == 0:
        return linear_eqn(b,c)

    D = b ** 2 - 4 * a * c
    x1 = None
    x2 = None

    if D>0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
    if D == 0:
        x1 = x2 = -b / (2 * a)
    if D<0:
        x1 = x2 = None

    return x1, x2
print(solve_quadratic_eqn(0, -5, 6))


#8.Declare a function named print_list
# It takes a list as a parameter and it prints out each element of the list

# def print_list(list):
#     for element in list:
#         print(element)
#
# print_list([1,2,3,4,5,6,7])

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)

def reverse_list(massive):
    for element in reversed(massive):
        print(element)

reverse_list([1,2,3,4,5])

# def reverse_list_massive(massive):
#         print(massive[::-1])
#
# reverse_list_massive([1,2,3,4,5])

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    c_lst = []
    for item in lst:
        c_lst.append(item.capitalize())
    return c_lst

fruits = ['apple', 'banana', 'orange']
print(capitalize_list_items(fruits))

#short method from GPT:
# def capitalize_list_items(lst):
#     return [item.capitalize() for item in lst]

#11.Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end

def add_item(lst, item):
    lst.append(item)
    return lst

print(add_item(fruits, 'cherry'))

#12. Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it

def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(fruits, 'cherry'))

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range

def sum_of_numbers(nums):
    sum = 0
    for num in range(nums+1):
        sum += num
    return sum

print(sum_of_numbers(100))

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range

def sum_of_even(nums):
    sum = 0
    for num in range(nums+1):
        if num % 2 == 0:
            sum += num
    return sum
print(sum_of_even(10))

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range

def sum_of_odd(nums):
    sum = 0
    for num in range(nums+1):
        if num % 2 != 0:
            sum += num
    return sum

print(sum_of_odd(10))

#Level 2.
#1. Declare a function named evens_and_odds . It takes a positive integer as parameter
# and it counts number of evens and odds in the number

def evens_and_odds(nums):
    evens_lst = []
    odds_lst = []
    for num in range(nums+1):
        if num % 2 == 0:
            evens_lst.append(num)
        if num % 2 != 0:
            odds_lst.append(num)
    return len(evens_lst), len(odds_lst)

nums = 100
print(f"evens and odds in range {nums}: {evens_and_odds(100)}")

# def function():
    # Main goals of function:
    # 1) Make some action
    # 2) Return something


#2.Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    if number<0:
        return "Factorial is not defined for negative numbers"
    if number==0:
        return 1
    else:
        result=1
        for i in range(1, number+1):
            result *=i
        return result

number = 6
print(f"The factorial of {number} is {factorial(number)}")

#google solution
# import math
#
# number = 5
# result = math.factorial(number)
# print(f"The factorial of {number} is {result}")

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(lst):
    if len(lst) == 0:
        return ("is empty")
    else:
        return ("is not empty")

print(is_empty([1,2,3,4,5,6,7]))
print(is_empty([]))

#4. Write a function called greet which takes a default argument, name.
# If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name

def greet (name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")

#5. Create a function called show_args to take an arbitrary number of named arguments and print their names and values

def show_args(**args):
    for k,v in args.items():
        print(f"{k}: {v}")

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

#Exercises: Level 3
#1.Write a function called is_prime, which checks if a number is prime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

print(is_prime(19))

#2. Write a functions which checks if all items are unique in the list

def is_unique(lst,i):
    if lst.count(i) ==1:
        return True
    else:
        return False

fruits = ['apple', 'banana', 'orange', 'cherry', 'banana']
print(is_unique(fruits, 'cherry'))

#3.Write a function which checks if all the items of the list are of the same data type

def same_type(lst):
    if len(lst)==0:
        return "is empty"
    first_item_type = type(lst[0])
    for item in lst[1:]:
        if type(item) == first_item_type:
            return True
        else:
            return False

# lst = []
# lst = ['apple', 'banana', 'orange', 'cherry', 'banana']
lst = ['Asabeneh', 250, True, False, {'country': 'Finland', 'city': 'Helsinki'}]
print(same_type(lst))

#4.Write a function which check if provided variable is a valid python variable

import keyword
def is_valid_variable(name):
    return name.isidentifier() and keyword.iskeyword(name)

print(is_valid_variable("%ccuws"))
print(is_valid_variable("54ccuws"))
print(is_valid_variable("Asab_4"))

#5.Go to the data folder and access the countries-data.py file:
#Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order

from countries_data import

def most_spoken_languages

































