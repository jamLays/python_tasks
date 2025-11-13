#23. Use index or find to find the position of the first occurrence of the word 'because'
# in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent='You cannot end a sentence with because because because is a conjunction'
sub='because'
print('23.',sent.index(sub))
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence
print('24.',sent.rindex('because'))
#25. Slice out the phrase 'because because because' in the following sentence
slice=sent[0:30]+sent[54:71]
print('25.',slice)
#26.Find the position of the first occurrence of the word 'because' in the following sentence
print('26.',sent.find('because'))
#28. Does ''Coding For All' start with a substring Coding?
coding='Coding For All'
print('28.',coding.startswith('Coding'))
#29.Does 'Coding For All' end with a substring coding?
print('29.',coding.endswith('coding'))
#30.'   Coding For All      '  , remove the left and right trailing spaces in the given string
coding_for_strip ='   Coding For All      '
print('30.',coding_for_strip.strip(' '))

#31.Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

#The isidentifier() method returns True if the string is a valid identifier, otherwise False.
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces

first_sent='30DaysOfPython'
second_sent='thirty_days_of_python'
print('31.',first_sent.isidentifier())
print(second_sent.isidentifier())

#32.The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
python_library =['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('32.', '# '.join(python_library))

#33. Use the new line escape sequence to separate the following sentences
first_st= 'I am enjoying this challenge.'
second_st = 'I just wonder what is next.'
print('33.', first_st +'\n'+second_st)

#34.Use a tab escape sequence to write the following lines
print('Name  \tAge \tCountry \tCity')
print('Asabeneh\t250\tFinland  \tHelsinki')

#35.Use the string formatting method to display the following:
radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)

#36. Make the following using string formatting methods:
a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')





