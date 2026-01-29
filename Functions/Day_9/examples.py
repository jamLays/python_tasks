a =22
if a>0 and a%2 ==0:
    print('A is an even and positive integer')
elif a>0 and a%2 !=0:
    print('A is a positive integer')
elif a==0:
    print('A is zero')
else:
    print('A is a negative integer')


user = 'John'
access_level = 3
if user == 'Nancy' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')



score = 51
attendance =78
submitted = False

if score >= 60:
    if attendance >= 80:
        if submitted:
            print ('Pass with good standing')
        else:
            print ('Pass but missing assignment')
    else:
        print ('Pass but low attendance')
else:
    print ('Fail')

import random
coin1 = bool(random.randint(0, 1))
coin2 = bool(random.randint(0, 1))

print('coin1', coin1)
print('coin2', coin2)

if coin1 and coin2:
    print('Yes')
else:
    print('No')

print('0 - False, 1 - True')

experiense = bool(int(input('experiense: ')))
education = bool(int(input('education: ')))
test_passed = bool(int(input('test_passed: ')))

if experiense:
    # если есть опыт
    if test_passed:
        # если выполнил тестовое задание (есть опыт)
        print('interview')

    else:
        # иначе (не выполнил тестовое задание) (есть опыт)
        print('reject')

else:
    # иначе (нет опыта)
    if education:
        # если есть образование (нет опыта)
        if test_passed:
            # если выполнил тестовое задание (нет опыта)
            print('interview')

        else:
            # иначе (не выполнил тестовое задание) (есть опыт)
            print('reject')

    else:
        # иначе (нет образования) (нет опыта)
        print('reject')

