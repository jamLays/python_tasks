#1. Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero = [i for i in numbers if i<=0]
print(negative_zero)

#2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list = [number for row in list_of_lists for number in row]
print(list)

#3. Using list comprehension create the following list of tuples:

#4. Flatten the following list to a new list:
#Iterables: list, dict, tuple, and set

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[0:3].upper(),city.upper()] for sublist in countries for country,city in sublist]
print(output)

# for country in countries:
#     for i in country:
#         for str in i:
#             print(str.upper())

#5. Change the following list to a list of dictionaries:
output_2 = [{'country':country.upper(), 'city':city.upper()} for sublist in countries for country,city in sublist]
print(output_2)

#6. Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [(name + ' ' + first_name) for sublist in names for name, first_name in sublist]
print(output)

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.

y = lambda a, x, b: a*x + b
print(y(1,6,8))




