#WHILE zaLOOP
# count = 0
# while count < 5:
#     print (count)
#     count += 1
# else:
#     print (count)
#from os import WCONTINUED

#Break
# count = 0
# while count < 7:
#     print (count)
#     count += 1
#     if count == 4:
#         print(count)
#         break
#
# Continue
# count = 0
# while count < 5:
#     if count == 2:
#         count += 1
#     continue
# print(count)
# count = count + 1

#for in list
# numbers = [0, 1, 2, 3, 4, 5]
# for i in numbers:
#     print(i)
#
# #for in string
# language = 'Python'
# for l in language:
#     print(l)
# for i in range(len(language)): #range makes len(language) iterable
#     print(i)
#
# #for in tuple
# numbers = (0, 1, 2, 3, 4, 5)
# for i in numbers:
#     print(i)

#for in dct
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
#
# for key in person:
#     print(key)
#
# for key, value in person.items():
#     print(key, ':', value)

#for in sets
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)

#break for data types
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         break

# for data types (not full understand)
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

#Range Function
# lst = list(range(11))
# print(lst)

#range() function is used to return a list of numbers. The range(start, end, step) takes three parameters:
# starting, ending and increment. By default it starts from 0 and the increment is 1. But actually in result end of range will be - value-1,
#not including end
# The range sequence needs at least 1 argument (end). Creating sequences using range

# st = set(range(1,11))
# print(st)
#
# lst = list(range(0,13,2))
# print(lst)

#for backward from start to end
# lst = list(range(11,0,-2))
# print(lst)

#for iterator in range(start, end, step):
# for number in range(11):
#     print(number)

#Nested For Loop
# syntax
#for x in y:
    #for t in x:
        #print(t)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)

# for skill in person['skills']:
#     print(skill)

# for number in range(1, 11):
#     print('number', number)
# else:
#     print('The loop stops at', number)

for number in range(6):
    pass








