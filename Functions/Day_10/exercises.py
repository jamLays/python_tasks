#1. Iterate 0 to 10 using for loop, do the same using while loop
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print(count)

#2.Iterate 10 to 0 using for loop, do the same using while loop
count = 10
# while count >0:
#     print(count)
#     count -= 1
# else:
#     print(count)

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

# count = '#'
# while count < '#######':
#     print(count)
#     count = count + '#'
# else:
#     print(count)

#4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

# first = ['# # # #', '# # # #']
# second = ['# # # #', '# # # #','# # # #','# # # #']
# for number in first:
#     for number2 in second:
#         print(number, number2)
#
#5. Print the following pattern:
# before = ['0 x 0']
# after = [' = 0']
# for number in before:
#     for number2 in after:
#         print(number, number2)




#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items
# lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for i in lst:
#     print(i)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
# count = 0
# while count <100:
#     count += 1
#     if count %2 == 0:
#         print(count)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers

# count = 0
# while count <100:
#     count += 1
#     if count % 2 != 0:
#         print(count)


#Exercises: Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers

# total_sum=0
# for i in range(100):
#     total_sum = total_sum +i
# print(total_sum+100)

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds
# total_sum_evens=0
# total_sum_odds=0
#
# for i in range(101):
#     if i % 2 == 0:
#         total_sum_evens = total_sum_evens + i
#     if i % 2 != 0:
#         total_sum_odds = total_sum_odds + i
# print(total_sum_evens, total_sum_odds)

#3. Exercises: Level 3
#1. Go to the data folder and use the countries.py file
# Loop through the countries and extract all the countries containing the word land

#from countries import countries
# for country in countries:
#     if 'land' in country.lower(): # lower - независимость от регистра
#         print(country)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop
# fruits = ['banana', 'orange', 'mango', 'lemon']
# for i in range(len(fruits)-1, -1,-1):
#     print(fruits[i])

#3.1 Go to the data folder and use the countries_data.py file
all_languages = []
from countries_data import countries
for country in countries:
    all_languages.extend(country['languages'])
print(all_languages)
unique = set(all_languages)
print(unique)
print(len(unique))


#3.2 Find the ten most spoken languages from the data
from collections import Counter
all_languages = []
from countries_data import countries
for country in countries:
    all_languages.extend(country['languages'])
print(all_languages)
number_all_lang = Counter(all_languages)
print(number_all_lang)
most_common_languages = number_all_lang.most_common(10)
print(most_common_languages)

#3.3 Find the 10 most populated countries in the world
sorted_by_popu = sorted(countries, key = lambda x: x['population'], reverse = True)
print(sorted_by_popu)
top_10_populated = sorted_by_popu[:10]
print(top_10_populated)
for i in top_10_populated:
    print(i['name'], i['population'])










