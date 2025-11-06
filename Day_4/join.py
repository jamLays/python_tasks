# challenge = 'Coding', 'For' , 'All'
# print(challenge)
# print(type(challenge))
#
# result = ' '.join(challenge)
# print(result)
import string
from typing import final


# Return a version of the string where each word is titlecased.
# More specifically, words start with uppercased characters and all remaining cased characters have lower case.

#1. split according to separator ' '
#2. capitalize each substring
#3. transform list (after split) into string
#4.return string

def create_title(string):
    step_1=string.split(' ')
    y=''

    for x in step_1:
        step_2=x.capitalize()
        y=y+step_2+' '  #y+=step_2

    return y.strip()

input = 'united states werty ghy'


result1 = input.title()
result2 = create_title(input)

print(result1 == result2)

input2 = 'united states sqwe'

result3 = input2.title()
result4 = create_title(input2)

print(result3 == result4)