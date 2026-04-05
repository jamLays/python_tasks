#Importing a Module

import my_module

print(my_module.full_name('Leysa', 'Yami'))

#Import Functions from a Module

from my_module import full_name
print(full_name('Leysa', 'Yami'))


# from Functions.Day_11.exercises import factorial
# print(factorial(5))
#printing all results from Day_11.exercises because there are print, importing it's just perenos

from my_module import full_name as name

print(name('Lelya', 'Dear'))


from my_module import add_two_numbers
print(add_two_numbers(10, 35))

from my_module import add_two_numbers as sum
print(sum(10, 35))

#OS Module
#for creating, changing current working directory, and removing a directory (folder),
# fetching its contents, changing and identifying the current directory

import os
# creating a directory
# os.mkdir ('directory_name')
#
# #Changing the current directory
# os.chdir('path')
#
# #Getting current working directory
# os.getcwd()
#
# # Removing directory
# os.rmdir()

#Sys Module
# import sys
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
#
# # to exit sys
# sys.exit()
# # To know the largest integer variable it takes
# sys.maxsize
# # To know environment path
# sys.path
# # To know the version of python you are using
# sys.version


#Statistics Module

from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))


#Math Module
import math
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)
print(sqrt(2))
print(pow(2,3))
print(floor(9.81))
print(ceil(9.81))
print(log10(100))

from math import pi as PI
print(PI)

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

from random import random, randint
print(random()) #it returns a value between 0 and 0.9999
print(randint(8,17)) #it returns a random integer number between [] inclusive

# Игра "Угадай число":

import random
num = random.randint(1,100)

guess = int(input("Guess a number between 1 and 100: "))


if num == guess:
    print("Correct!")
if num > guess:
        print("Too high!")
if num < guess:
            print("Too low!")




















