from functools import reduce

INITIAL_COUNTRIES = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
INITIAL_NAMES = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
INITIAL_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#1. Use for loop to print each country in the countries list

# for i in countries:
#     print(i)
#
# for j in names:
#     print(j)
#
# for k in numbers:
#     print(k)

#Level 2
#1. Use map to create a new list by changing each country to uppercase in the countries list
def change_upper(country):
    return country.upper()


country_upper = map(change_upper, INITIAL_COUNTRIES)
print('1.', list(country_upper))


#2. Use map to create a new list by changing each number to its square in the numbers list
def square_number(num):
    return num ** 2


numbers = map(square_number, INITIAL_NUMBERS)
print('2.', list(numbers))


#3. Use map to change each name to uppercase in the names list
def change_names_upper(name):
    return name.upper()


names_upper = map(change_names_upper, INITIAL_NAMES)
print('3.', list(names_upper))


#4. Use filter to filter out countries containing 'land'
def land_filter(country):
    if 'land' in country:
        return True
    return False


filtered_countries = filter(land_filter, INITIAL_COUNTRIES)
print('4.', list(filtered_countries))


#5. Use filter to filter out countries having exactly six characters
def six_charecters(country):
    if len(country) == 6:
        return True
    return False


filtered_countries = filter(six_charecters, INITIAL_COUNTRIES)
print('5.', list(filtered_countries))


#6. Use filter to filter out countries containing six letters and more in the country list
def is_country_long(country):
    if len(country) >= 6:
        return True
    return False


filtered_countries = filter(is_country_long, INITIAL_COUNTRIES)
print('6.', list(filtered_countries))


#7. Use filter to filter out countries starting with an 'E'
def start_with_character(country):
    if country.startswith('E'):
        return True
    return False


filtered_countries = filter(start_with_character, INITIAL_COUNTRIES)
print('7.', list(filtered_countries))


#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
#8.1  Отфильтровать страны с буквой 'e' и привести к верхнему регистру

def country_has_e(country):
    if 'e' in country:
        return True
    return False


filtered_countries = filter(country_has_e, INITIAL_COUNTRIES)


def to_upper(country):
    return country.upper()


result = map(to_upper, filtered_countries)
print('8.1', list(result))


#8.2 Взять длинные страны (> 6 букв) и посчитать сумму их длин
def long_countries(country):
    return len(country) > 6

filtered_countries = list(filter(long_countries, INITIAL_COUNTRIES))

def get_len(sum, next_country):
    print('reduce', sum, next_country)
    return sum + len(next_country)

print('8.2', reduce(get_len, filtered_countries, 0))

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items

def get_string_lists(list):
    return map(str, list)


print('9.1', list(get_string_lists(INITIAL_NUMBERS)))
print('9.2', list(get_string_lists(INITIAL_COUNTRIES)))
print('9.3', list(get_string_lists(INITIAL_NAMES)))

#10. Use reduce to sum all the numbers in the numbers list

sum_all = reduce(lambda x, y: x + y, INITIAL_NUMBERS)
print('10', sum_all)

#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway,
# and Iceland are north European countries

sum_sentence = reduce(lambda x, y: x + ',' + y, INITIAL_COUNTRIES)
final_sentence = sum_sentence + ' are north European countries'
print('11', final_sentence)

#12. Declare a function called categorize_countries that returns a list of countries with
# some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan'))

