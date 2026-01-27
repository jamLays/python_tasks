 #1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
 # If below 18 give feedback to wait for the missing amount of years. Output:

 #1. Enter your age: 30
 # You are old enough to learn to drive.
 # Output:
 # Enter your age: 15
 # You need 3 more years to learn to drive.

# age = input("Enter your age: ")
# if int(age) >= 18:
#     print('1.', "You are old enough to learn to drive")
# else:
#     print('1.', "You need 3 more years to learn to drive")

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# my_age = 26
# your_age = int(input("Enter your age: "))
# difference = your_age - my_age
# if difference ==1:
#     print("There is 1 year difference")
# elif difference>1:
#     print("There is", difference, "years difference")
# else:
#     print("There is no difference")

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b. Output:
# number_1 = int(input("Enter a number 1: "))
# number_2 = int(input("Enter a number 2: "))
# if number_1 > number_2:
#     print(number_1, "is greater than", number_2)
# elif number_1<number_2:
#     print(number_1, "is less than", number_2)
# else:
#     print(number_1, "is equal to", number_2)

#Level 2.
 # 1. Write a code which gives grade to students according to theirs scores:
 # 90-100, A
 # 80-89, B
 # 70-79, C
 # 60-69, D
 # 0-59, F

# grade = int(input("Enter grade: "))
# if grade >=90 and grade <= 100:
#     print("Grade is A")
# elif grade >=80 and grade <= 89:
#     print("Grade is B")
# elif grade >=70 and grade <= 79:
#     print("Grade is C")
# elif grade >=60 and grade <= 69:
#     print("Grade is D")
# elif grade >=0 and grade <= 59:
#     print("Grade is F")

#2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
 # If the user input is: September, October or November, the season is Autumn.
 # December, January or February, the season is Winter. March, April or May, the season is Spring June,
 # July or August, the season is Summer

# month = input("Enter month: ")
# if month == 'December' or month == 'January' or month == 'February':
#     print('the season is Winter')
# elif month == 'March' or month == 'April' or month == 'May':
#     print('the season is Spring')
# elif month == 'June' or month == 'July' or month == 'August':
#     print('the season is Summer')
# elif month == 'September' or month == 'October' or month == 'November':
#     print('the season is Autumn')

#3.If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
 # If the fruit exists print('That fruit already exist in the list')

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input('Enter fruit name: ')
# if fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fruit)
#     print(fruits)

#4. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 # If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node,
 # Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
 # Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 # If the person is married and if he lives in Finland, print the information in the following format:
 # Asabeneh Yetayeh lives in Finland. He is married

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list
if 'skills' in person:
    print(person['skills'][2])

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
    else:
        print('There is no what I need')

#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node,
 # Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
 # Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

#it's my solution:
if 'JavaScript' and 'React' in person:
     print('He is a front end developer')
if 'Node' and 'Python' and 'MongoDB' in person and 'React' not in person:
     print('He is a backend developer')
if 'React' and 'Node' and 'MongoDB' in person:
         print('He is a fullstack developer')
else:
     print('unknown title')

#it's GPT' solution through my understanding:
skills_set = person.get('skills', [])
if {'JavaScript', 'React'} in skills_set:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set) and 'React' not in skills_set:
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB', 'Python'}.issubset(skills_set):
    print('He is a fullstack developer')
else:
    print('unknown title')

# If the person is married and if he lives in Finland, print the information in the following format:
 # Asabeneh Yetayeh lives in Finland. He is married

if person.get('is_married'):
    if person.get('country')=='Finland':
        print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married")










