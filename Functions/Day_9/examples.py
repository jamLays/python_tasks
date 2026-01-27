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


